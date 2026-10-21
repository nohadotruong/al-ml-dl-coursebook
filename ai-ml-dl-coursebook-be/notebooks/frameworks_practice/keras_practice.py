# Use high level API of TensorFlow for below example
# Import libraries
import numpy as np  # For arrays and numerical operations
from tensorflow.keras.models import Sequential  # Sequential model API
from tensorflow.keras.layers import Dense  # Dense (fully connected) layer
from tensorflow.keras.optimizers import Adam  # Adam optimizer
from tensorflow.keras.callbacks import Callback  # For monitoring training
import matplotlib.pyplot as plt  # For plotting data


# Prepare data
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # Input feature
y = np.array([1, 3, 7, 8, 12, 12, 16, 18, 21, 22, 26])  # Target variable

# Build the model
model = Sequential(
    [Dense(1, input_shape=(1,))]  # Single neuron, input is 1D (x), output is 1D (y)
)

# Compile the model
model.compile(
    optimizer=Adam(learning_rate=0.01),  # Adam optimizer for gradient updates
    loss="mean_squared_error",  # Loss function: MSE for regression
)


# Define a callback to monitor training
class MyCallback(Callback):
    def on_epoch_end(self, epoch, logs=None):
        if epoch % 100 == 0:
            print(f"Epoch {epoch}, Loss: {logs['loss']}")


# Epoch 0, Loss: 428.3687744140625
# Epoch 100, Loss: 205.87892150878906
# Epoch 200, Loss: 85.93122863769531
# Epoch 300, Loss: 30.960357666015625
# Epoch 400, Loss: 10.014851570129395
# Epoch 500, Loss: 3.492849588394165
# Epoch 600, Loss: 1.821825385093689
# Epoch 700, Loss: 1.43678617477417
# Epoch 800, Loss: 1.320535659790039
# Epoch 900, Loss: 1.2488142251968384


# Train the model
model.fit(
    x,
    y,  # Training data
    epochs=1000,  # Train for 1000 iterations
    verbose=0,  # Suppress default training logs
    callbacks=[MyCallback()],  # Use custom callback
)

# Make predictions
y_pred = model.predict(x)  # Predict y values for all x using trained model

# Visualize predictions vs actual data
plt.scatter(x, y, color="blue", label="Actual data")  # Plot actual data points
plt.plot(x, y_pred, color="red", label="Predicted data")  # Plot regression line
plt.xlabel("X")  # x-axis label
plt.ylabel("Y")  # y-axis label
plt.legend()  # Show legend
plt.title("Linear Regression: Actual vs Predicted")  # Plot title
plt.show()  # Display the plot
