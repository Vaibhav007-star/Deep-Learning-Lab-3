"""
Lab 3
Implement a Feedforward Neural Network using PyTorch

"""

# Import required libraries
import torch
import torch.nn as nn
import torch.optim as optim

# -----------------------------
# Step 1: Create Dataset
# -----------------------------
# AND Logic Gate Dataset

X = torch.tensor([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
], dtype=torch.float32)

y = torch.tensor([
    [0],
    [0],
    [0],
    [1]
], dtype=torch.float32)

# -----------------------------
# Step 2: Define Neural Network
# -----------------------------
class FeedforwardNN(nn.Module):
    def __init__(self):
        super(FeedforwardNN, self).__init__()

        # Input Layer (2 neurons) -> Hidden Layer (4 neurons)
        self.fc1 = nn.Linear(2, 4)

        # Activation Function
        self.relu = nn.ReLU()

        # Hidden Layer (4 neurons) -> Output Layer (1 neuron)
        self.fc2 = nn.Linear(4, 1)

        # Output Activation
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.sigmoid(x)
        return x


# -----------------------------
# Step 3: Create Model
# -----------------------------
model = FeedforwardNN()

# Binary Cross Entropy Loss
criterion = nn.BCELoss()

# Adam Optimizer
optimizer = optim.Adam(model.parameters(), lr=0.01)

# -----------------------------
# Step 4: Train the Model
# -----------------------------
epochs = 100

print("Training Started...\n")

for epoch in range(epochs):

    # Forward Pass
    outputs = model(X)

    # Calculate Loss
    loss = criterion(outputs, y)

    # Backpropagation
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    # Print Loss Every 10 Epochs
    if (epoch + 1) % 10 == 0:
        print(f"Epoch [{epoch+1}/{epochs}]  Loss = {loss.item():.4f}")

print("\nTraining Completed!")

# -----------------------------
# Step 5: Test the Model
# -----------------------------
print("\nPredictions:\n")

with torch.no_grad():

    predictions = model(X)

    for i in range(len(X)):
        predicted_probability = predictions[i].item()
        predicted_class = 1 if predicted_probability >= 0.5 else 0

        print(
            f"Input: {X[i].tolist()} "
            f"=> Probability: {predicted_probability:.4f} "
            f"=> Predicted Class: {predicted_class}"
        )