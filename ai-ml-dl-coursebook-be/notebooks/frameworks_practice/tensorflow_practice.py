# Use low level API of TensorFlow for below example
# Import libraries
import numpy as np  # For numerical operations and arrays
import tensorflow as tf  # TensorFlow for low-level ML operations
import matplotlib.pyplot as plt  # For plotting data and predictions

# Prepare data
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # Input feature
y = np.array([1, 3, 7, 8, 12, 12, 16, 18, 21, 22, 26])  # Target variable

# Initialize model parameters
W = tf.Variable(tf.random.normal([1]), name="weight")  # Weight, trainable parameter
b = tf.Variable(tf.random.normal([1]), name="bias")  # Bias, trainable parameter


# Define the model (forward pass)
def linear_regression(x):
    """
    Linear model: y_pred = W * x + b
    """
    return W * x + b


# Define the loss function
def loss(y_true, y_pred):
    """
    Mean Squared Error (MSE)
    Measures difference between predicted and actual values
    """
    return tf.reduce_mean(tf.square(y_true - y_pred))


# Define the optimizer
optimizer = tf.optimizers.Adam(learning_rate=0.01)  # Adam optimizer to update W and b


# Define a single training step
def train_step(x, y):
    """
    Performs one gradient update step
    """
    with tf.GradientTape() as tape:  # Record operations for automatic differentiation
        y_pred = linear_regression(x)  # Forward pass: compute predictions
        current_lost = loss(y, y_pred)  # Compute loss
    gradients = tape.gradient(current_lost, [W, b])  # Compute gradients w.r.t W and b
    optimizer.apply_gradients(
        zip(gradients, [W, b])
    )  # Update parameters using gradients
    return current_lost


# Training loop
epochs = 1000
for epoch in range(epochs):
    current_loss = train_step(x, y)  # Perform one training step
    if epoch % 100 == 0:  # Print progress every 100 epochs
        print(f"Epoch {epoch}, Loss: {current_loss.numpy()}")

# Output shows loss decreasing as model learns:
# Epoch 0, Loss: 535.03
# Epoch 100, Loss: 280.11
# ...
# Epoch 900, Loss: 1.84

# Make predictions
y_pred = linear_regression(x)  # Predict using trained W and b

# Visualize predictions vs actual data
plt.scatter(x, y, color="blue", label="Actual data")  # Plot actual data points
plt.plot(x, y_pred, color="red", label="Predicted data")  # Plot regression line
plt.xlabel("X")  # x-axis label
plt.ylabel("Y")  # y-axis label
plt.legend()  # Show legend
plt.title("Linear Regression: Actual vs Predicted")  # Plot title
plt.show()  # Display the plot
