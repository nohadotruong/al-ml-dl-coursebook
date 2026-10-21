import torch
import numpy as np

# Create tensors
# Create a 1D tensor from a Python list
tensor_a = torch.Tensor([1, 2, 3, 4, 5, 6])
# tensor_a: [1, 2, 3, 4, 5, 6], dtype=float32 by default

# Create a tensor from a NumPy ndarray
arr = np.array([[1, 2, 3], [4, 5, 6]])
tensor_b = torch.from_numpy(arr)
# tensor_b: same values as arr, shares memory with arr (changing one affects the other)

# Create a tensor filled with zeros
tensor_c = torch.zeros(2, 3)
# tensor_c: 2x3 tensor with all zeros

# Create a tensor filled with ones
tensor_d = torch.ones(2, 3)
# tensor_d: 2x3 tensor with all ones

# Create a tensor with random values sampled from standard normal distribution N(0,1)
tensor_e = torch.randn(2, 3)
# tensor_e: 2x3 tensor, random values

# Print all tensors
print(tensor_a, tensor_b, tensor_c, tensor_d, tensor_e)

# Compute with tensors
# Add a scalar to a tensor
print(tensor_b + 1)
# Adds 1 to every element of tensor_b

# Add two tensors element-wise
print(tensor_b + tensor_e)
# Each element of tensor_b is added to corresponding element of tensor_e

# Check shape of tensor
print(tensor_b.shape)
# tensor_b.shape: torch.Size([2, 3])

# Reshape tensors
# Flatten tensor to 1D
flat_b = tensor_b.flatten()
print(flat_b, flat_b.shape)
# flat_b: [1,2,3,4,5,6], shape: torch.Size([6])

# Add a dimension (unsqueeze)
unsq_b = tensor_b.unsqueeze(0)
print(unsq_b, unsq_b.shape)
# Adds a new dimension at index 0 → shape: [1, 2, 3]

# Remove a dimension (squeeze)
sq_b = unsq_b.squeeze(0)
print(sq_b, sq_b.shape)
# Removes dimension 0 → shape back to [2, 3]

# Another squeeze example (no dimension removed if size >1)
per_b = unsq_b.squeeze(0)
print(per_b, per_b.shape)
# Same as sq_b: [2, 3]

# Summary
# Create tensors
#   From Python lists: torch.Tensor()
#   From NumPy arrays: torch.from_numpy()
#   Pre-filled tensors: torch.zeros(), torch.ones()
#   Random tensors: torch.randn()
# Basic computations
#   Tensor + scalar → broadcast addition
#   Tensor + tensor → element-wise addition
#   shape shows tensor dimensions
# Reshape / modify dimensions
#   flatten() → 1D tensor
#   unsqueeze(dim) → add a new dimension
#   squeeze(dim) → remove a dimension of size 1
