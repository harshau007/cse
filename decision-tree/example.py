import numpy as np
from DecisionTree import DecisionTree  # Assuming the DecisionTree implementation is saved in decision_tree.py
from sklearn.model_selection import train_test_split

# Example usage of the DecisionTree class
# Load a dataset (for example, dataset from sklearn: load_iris, load_wine, load_breast_cancer, load_digits)
from sklearn.datasets import load_digits

# Load dataset
data = load_digits()
X = data.data
y = data.target

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Convert y_train and y_test to NumPy arrays (if necessary)
y_train = np.array(y_train)
y_test = np.array(y_test)

# Initialize and train the DecisionTree classifier
dt = DecisionTree(max_depth=3)
dt.fit(X_train, y_train)

# Make predictions on the test set
y_pred = dt.predict(X_test, y_train)

# Evaluate the model
evaluation_results = dt.evaluate(X_test, y_test)
print("Evaluation Results:", evaluation_results)

# Predict for a specific instance
sample = X_test[0].reshape(1, -1)
predicted_class = dt.predict(sample, y_train)
print("Predicted class for sample:", predicted_class)
