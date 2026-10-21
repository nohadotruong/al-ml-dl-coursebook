import tensorflow as tf  # Import TensorFlow for tensor operations and GPU computing
import numpy as np  # Import NumPy to help create arrays for tensors


# Tensor initialization
tensor_1d = tf.constant([1, 2, 3, 4])  # 1D tensor (vector)
tensor_2d = tf.constant(np.array([[1, 2], [3, 4]]))  # 2D tensor (matrix)
zeros_tensor = tf.zeros([2, 3])  # 2x3 tensor filled with zeros
ones_tensor = tf.ones([2, 3])  # 2x3 tensor filled with ones

# print(tensor_1d)
# print(tensor_2d)
# print(zeros_tensor)
# print(ones_tensor)

# Basic Tensor Operations

a = tf.constant([1, 2, 3])
b = tf.constant([4, 5, 6])

add = tf.add(a, b)  # Element-wise addition → [5, 7, 9]
subtract = tf.subtract(a, b)  # Element-wise subtraction → [-3, -3, -3]
multiply = tf.multiply(a, b)  # Element-wise multiplication → [4, 10, 18]
divide = tf.divide(a, b)  # Element-wise division → [0.25, 0.4, 0.5]


# print(add, subtract, multiply, divide)

# Check for GPU availability
print("Num GPUs Available: ", len(tf.config.list_physical_devices("GPU")))

# Using GPU for computation
with tf.device("/GPU:0"):
    tensor = tf.constant([[1.0, 2.0], [3.0, 4.0]])
    result = tf.matmul(tensor, tensor)  # Matrix multiplication
    print(result)
