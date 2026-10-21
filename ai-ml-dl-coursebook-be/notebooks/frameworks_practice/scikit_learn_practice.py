# Find a rule to approximate (or predict) the value of Y given X

# Import libraries
import numpy as np  # For numerical operations and arrays
import matplotlib.pyplot as plt  # For plotting graphs
from sklearn.linear_model import LinearRegression  # The linear regression model

# Define the dataset
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # Input variable (feature)
y = np.array([1, 3, 7, 8, 12, 12, 16, 18, 21, 22, 26])  # Output variable (target)

# Visualize the raw data points
plt.title("Data points")
plt.scatter(x, y)  # Scatter plot: each point shows X vs Y
plt.xlabel("X")  # Label for x-axis
plt.ylabel("Y")  # Label for y-axis
plt.show()  # Display the plot

# Prepare the model
model = LinearRegression()  # Create a Linear Regression model instance
x = x.reshape(-1, 1)  # Reshape x from 1D to 2D array (required by scikit-learn)

# Train the model
model.fit(x, y)  # Fit the linear regression model on the data
y_pred = model.predict(x)  # Predict Y values using the trained model

# Visualize the model’s predictions vs actual data
plt.scatter(x, y, color="blue", label="Actual data")  # Actual data points in blue
plt.plot(x, y_pred, color="red", label="Predicted data")  # Regression line in red
plt.xlabel("X")  # Label for x-axis
plt.ylabel("Y")  # Label for y-axis
plt.legend()  # Show legend
plt.title("Linear Regression: Actual vs Predicted")  # Title of plot
plt.show()  # Display the plot
