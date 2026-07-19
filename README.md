# Lab 3 - Feedforward Neural Network using PyTorch

## Objective

Implement a **Feedforward Neural Network (FNN)** using **PyTorch** to learn the **AND Logic Gate**.

---

##  Technologies Used

- Python 3.12+
- PyTorch
- Visual Studio Code
- Git & GitHub (Optional)

---

##  Project Structure

```
Lab-3/
│
├── .venv/                  # Virtual Environment (Not uploaded to GitHub)
├── lab3_feedforward_nn.py  # Main Python Program
├── README.md               # Project Documentation
└── .gitignore              # Ignore unnecessary files
```

---

##  What is a Feedforward Neural Network?

A Feedforward Neural Network (FNN) is one of the simplest types of Artificial Neural Networks.

- Data flows only in one direction.
- Input is passed through one or more hidden layers.
- The output layer predicts the final result.
- There are no loops or feedback connections.

Architecture:

```
Input Layer (2 Neurons)
        │
        ▼
Hidden Layer (4 Neurons)
     ReLU Activation
        │
        ▼
Output Layer (1 Neuron)
   Sigmoid Activation
        │
        ▼
Prediction
```

---

##  Dataset

This project uses the **AND Logic Gate**.

| Input 1 | Input 2 | Output |
|---------|---------|--------|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

---

## ⚙️ Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Lab-3.git
```

Replace `YOUR_USERNAME` with your GitHub username.

---

### Step 2: Open the Project Folder

```bash
cd Lab-3
```

---

### Step 3: Create a Virtual Environment

Windows

```bash
python -m venv .venv
```

---

### Step 4: Activate the Virtual Environment

PowerShell

```bash
.\.venv\Scripts\Activate.ps1
```

Command Prompt

```bash
.venv\Scripts\activate
```

---

### Step 5: Install PyTorch

```bash
python -m pip install torch
```

---

##  Run the Program

```bash
python lab3_feedforward_nn.py
```

---

##  Expected Output

```
Training Started...

Epoch [10/100] Loss = 0.65
Epoch [20/100] Loss = 0.51
...
Epoch [100/100] Loss = 0.07

Training Completed!

Predictions:

Input: [0.0, 0.0] -> Class: 0
Input: [0.0, 1.0] -> Class: 0
Input: [1.0, 0.0] -> Class: 0
Input: [1.0, 1.0] -> Class: 1
```

*The exact probabilities may vary because the model starts with random weights.*

---

##  Concepts Used

- Feedforward Neural Network
- Input Layer
- Hidden Layer
- Output Layer
- ReLU Activation Function
- Sigmoid Activation Function
- Binary Cross Entropy Loss (BCELoss)
- Adam Optimizer
- Forward Propagation
- Backpropagation
- Model Training
- Binary Classification

---

##  Code Workflow

1. Import required libraries.
2. Create the AND gate dataset.
3. Define the neural network architecture.
4. Initialize the model.
5. Define the loss function.
6. Define the optimizer.
7. Train the model for 100 epochs.
8. Make predictions.
9. Display the predicted classes.

---

##  Learning Outcomes

After completing this lab, you will understand:

- How a Feedforward Neural Network works.
- How to build a neural network using PyTorch.
- How forward propagation works.
- How backpropagation updates weights.
- How binary classification is performed.
- How to train and evaluate a simple neural network.

---

##  Author

**Vaibhav Lohchab**

B.Sc. Data Science & Artificial Intelligence

---

## 📄 License

This project is created for educational purposes only.
