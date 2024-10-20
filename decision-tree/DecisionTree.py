import numpy as np
from collections import Counter
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Function to calculate entropy
def entropy(y):
    """
    Calculate the entropy of the target variable (y).
    Computes entropy by summing the negative probabilities of each class multiplied by their log base 2.
    
    Args:
    y (np.array): Target variable array.
    
    Returns:
    float: Entropy value.
    """
    class_labels = np.unique(y)
    entropy_val = 0
    for label in class_labels:
        p = len(y[y == label]) / len(y)
        entropy_val += -p * np.log2(p)
    return entropy_val

# Function to calculate information gain for a feature
def information_gain(X, y, feature_idx):
    """
    Calculate the Information Gain by splitting on a particular feature.
    Calculates how much entropy decreases when splitting the dataset based on a feature.

    Args:
    X (np.array): Feature matrix.
    y (np.array): Target variable.
    feature_idx (int): Index of the feature to split on.

    Returns:
    float: Information gain for the feature.
    """
    # Entropy of the original dataset
    original_entropy = entropy(y)

    # Values and corresponding counts for the feature
    values, counts = np.unique(X[:, feature_idx], return_counts=True)

    # Weighted entropy of each subset
    weighted_entropy = 0
    for i, val in enumerate(values):
        subset_y = y[X[:, feature_idx] == val]
        weighted_entropy += (counts[i] / np.sum(counts)) * entropy(subset_y)

    # Information gain
    return original_entropy - weighted_entropy

# Decision Tree class
class DecisionTree:
    def __init__(self, max_depth=None):
        """
        Initialize the Decision Tree classifier.

        Args:
        max_depth (int): Maximum depth of the tree. If None, tree grows until all leaves are pure.
        """
        self.max_depth = max_depth
        self.tree = None

    def fit(self, X, y, depth=0):
        """
        Fit the Decision Tree classifier to the data.
        Recursively builds the tree by choosing the feature with the highest information gain at each node.

        Args:
        X (np.array): Feature matrix.
        y (np.array): Target variable.
        depth (int): Current depth of the tree.

        Returns:
        dict or int: The decision tree structure or the predicted class at a leaf node.
        """
        # Base cases (stopping criteria)
        if len(np.unique(y)) == 1:  # If all labels are the same
            return np.unique(y)[0]
        elif len(y) == 0:
            return
        elif self.max_depth is not None and depth >= self.max_depth:
            return np.bincount(y).argmax()  # Return majority class

        # Find the best feature to split on
        info_gains = [information_gain(X, y, i) for i in range(X.shape[1])]
        best_feature_idx = np.argmax(info_gains)
        
        # Split the data based on the best feature
        tree = {best_feature_idx: {}}
        feature_values = np.unique(X[:, best_feature_idx])
        for value in feature_values:
            X_subset = X[X[:, best_feature_idx] == value]
            y_subset = y[X[:, best_feature_idx] == value]
            tree[best_feature_idx][value] = self.fit(X_subset, y_subset, depth + 1)
        
        self.tree = tree
        return tree

    def predict(self, X, y_train):
        """
        Predict class labels for input data.
        Traverses the tree to make predictions based on input data.

        Args:
        X (np.array): Feature matrix for which to predict the labels.

        Returns:
        np.array: Predicted class labels.
        """
        # Helper function to traverse the tree
        def traverse_tree(x, tree, default_class):
            for key, branches in tree.items():
                feature_val = x[key]
                if feature_val in branches:
                    result = branches[feature_val]
                    if isinstance(result, dict):
                        return traverse_tree(x, result, default_class)
                    else:
                        return result
                else:
                    return default_class  # Handle unseen feature values by returning majority class

        # Determine the default class as the majority class from the training data
        default_class = Counter(y_train).most_common(1)[0][0]
        
        # Predict for each instance
        predictions = [traverse_tree(sample, self.tree, default_class) for sample in X]
        return np.array(predictions)

    def evaluate(self, X_test, y_test):
        """
        Evaluate the performance of the Decision Tree on the test set.

        Args:
        X_test (np.array): Feature matrix for the test set.
        y_test (np.array): True labels for the test set.

        Returns:
        dict: Dictionary containing accuracy, precision, recall, and F1-score.
        """
        y_pred = self.predict(X_test, y_test)
        results = {
            "accuracy": accuracy_score(y_test, y_pred),
            "precision": f"{precision_score(y_test, y_pred, average='macro')}",
            "recall": f"{recall_score(y_test, y_pred, average='macro')}",
            "f1_score": f"{f1_score(y_test, y_pred, average='macro')}"
        }
        return results
