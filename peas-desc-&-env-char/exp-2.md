# Experiment 02

## 02 A) PEAS Description

**Learning Objective:**  
Specify PEAS description for an AI agent.

**Tools:**  
MS Word

### Theory:

A problem-solving agent can be described formally by four components:

- **Performance Measure:** How happy the agent is with its performance
- **Environment:** Description of the world around
- **Actuator:** The actions taken by the agent
- **Sensor:** What the agent perceives

### Implementation:

**Problem Description:**  
There are `x` number of jugs with volumes (A, B,...Y) liters. None of the jugs have any measuring marks. There is a pump that can be used to fill the jugs with water. The goal is to get exactly `m` liters of water into the A liter jug, assuming an unlimited supply of water.

- **Performance Measure:** Maximum number of attempts by the user, shortest amount of moves, maximum capacity, and the amount of water used.
- **Environment:** A lab with a certain number of jugs and a tap with an unlimited amount of water.
- **Actuator:** The user who provides input to fill the jugs and the actual capacity of the jugs.
- **Sensor:** Overflow of water, both jugs filled.

### Learning Outcomes:

- **LO1:** Identify the problem for PEAS description.
- **LO2:** Describe the problem in PEAS form.

### Course Outcomes:

Upon completion of the course, students will be able to evaluate the various characteristics of Artificial Intelligence and Soft Computing techniques.

### Conclusion:

PEAS description helped us understand how an AI agent functions, its limitations, and how it interacts with the environment.

---

## 02 B) Environment Characteristics

**Learning Objective:**  
Specify environment characteristics for a toy/real-world problem.

**Tools:**  
MS Word

### Theory:

A problem can be characterized formally into six environment types:

- **Accessible/Fully Observable vs Partially Observable:**  
  If an agent's sensory apparatus gives it access to the complete state of the environment, we say that the environment is accessible. An accessible environment is convenient because the agent need not maintain any internal state to track the world.
- **Episodic vs Sequential:**  
  In an episodic environment, the agent's experience is divided into episodes. Each episode consists of the agent perceiving and then acting. The quality of its action depends just on the episode itself, as subsequent episodes do not depend on actions from previous episodes.

- **Static vs Dynamic:**  
  If the environment changes while the agent is deliberating, we call it dynamic. Otherwise, it is static. Static environments are easier to manage since the agent need not continuously monitor the world while deciding on an action. If time doesn't affect the environment but impacts the agent's performance score, the environment is semidynamic.

- **Discrete vs Continuous:**  
  If there are a limited number of distinct, clearly defined percepts and actions, we call the environment discrete.

- **Deterministic vs Stochastic:**  
  If the next state of the environment is completely determined by the current state and the agent's actions, we call it deterministic. However, if the environment is inaccessible, it may appear nondeterministic.

- **Single Agent vs Multi-Agent:**  
  This refers to whether an agent operates alone in the environment or with other agents.

### Implementation:

**Problem Description:**  
There are `x` number of jugs with volumes (A, B,...Y) liters. None of the jugs have any measuring marks. There is a pump that can be used to fill the jugs with water. The goal is to get exactly `m` liters of water into the A liter jug, assuming an unlimited supply of water.

- **Accessible/Fully Observable vs Partially Observable:** Fully observable, as the AI can see each state completely (i.e., the quantity of water filled in the jar).
- **Episodic vs Sequential:** Sequential, as the various steps in achieving the goal are noted and shown. One cannot directly go from the initial state to the goal state without prior information.

- **Static vs Dynamic:** Dynamic, as the water quantity continuously changes at every step.

- **Discrete vs Continuous:** Distinct, as the number of states can be around the actual water quantity required.

- **Deterministic vs Stochastic:** Deterministic, as the previous state can only lead to the next state until the goal state is reached.

- **Single Agent vs Multi-Agent:** Multi-agent, one is the user, and the other is the jar, which determines the next course of action.

### Learning Outcomes:

- **LO1:** Identify the problem.
- **LO2:** State the task environment.
