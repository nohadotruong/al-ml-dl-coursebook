# Find a rule to approximate (or predict) the value of Y given X

# Import libraries
import torch  # PyTorch main library
import torch.nn as nn  # For building neural network models
import torch.optim as optim  # Optimizers
import numpy as np  # Numerical operations and arrays
import matplotlib.pyplot as plt  # For plotting graphs


# Present data distribution of (X, Y)
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # Input feature (X)
y = np.array([1, 3, 7, 8, 12, 12, 16, 18, 21, 22, 26])  # Target variable (Y)

# Convert NumPy arrays to PyTorch tensors
# Use dtype=torch.float32 because nn.Linear expects float inputs
# unsqueeze(1) converts shape from [11] to [11,1] for a single feature
x_tensor = torch.tensor(x, dtype=torch.float32).unsqueeze(1)
y_tensor = torch.tensor(y, dtype=torch.float32).unsqueeze(1)

# Check tensor shapes
print(x_tensor.shape, y_tensor.shape)  # torch.Size([11,1]) torch.Size([11,1])


# Build model with torch.nn module
class LinearRegressionModel(nn.Module):
    def __init__(self):
        super(LinearRegressionModel, self).__init__()
        # Define a single linear layer: 1 input feature → 1 output
        self.fc = nn.Linear(in_features=1, out_features=1)

    def forward(self, x):
        # Forward pass: compute linear combination of input and weights
        output = self.fc(x)
        return output


# Create an instance of the model
model = LinearRegressionModel()

# Excute and model training monitor
criterion = nn.MSELoss()  # Mean Squared Error loss for regression
optimizer = optim.Adam(model.parameters(), lr=0.01)  # Adam optimizer

# Training loop
num_epochs = 2000
model.train()  # Set model to training mode

for epoch in range(num_epochs):
    # 1️⃣ Forward pass: compute model predictions
    outputs = model(x_tensor)

    # 2️⃣ Compute loss between predictions and true values
    loss = criterion(outputs, y_tensor)

    # 3️⃣ Backward pass: compute gradients
    optimizer.zero_grad()  # Clear previous gradients
    loss.backward()  # Backpropagate loss
    optimizer.step()  # Update weights

    # 4️⃣ Logging
    if epoch % 100 == 0:
        print(f"Epoch {epoch}, Loss: {loss.item():.4f}")


# Evaluation / prediction
model.eval()  # Set model to evaluation mode
with torch.no_grad():  # Disable gradient calculation for efficiency
    y_pred_tensor = model(x_tensor)  # Predict outputs for inputs


# Convert predictions to NumPy for plotting
y_pred = y_pred_tensor.numpy()

# Visualize predictions vs actual data
plt.scatter(x, y, color="blue", label="Actual data")  # Plot actual data points
plt.plot(x, y_pred, color="red", label="Predicted data")  # Plot regression line
plt.xlabel("X")  # x-axis label
plt.ylabel("Y")  # y-axis label
plt.legend()  # Show legend
plt.title("Linear Regression: Actual vs Predicted")  # Plot title
plt.show()  # Display the plot
