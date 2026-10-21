import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

# Show numbers of rows, columns
print(arr.shape)

# Reshape array
arr_reshape = arr.reshape(3, 2)
print(arr_reshape)

# Initial array
zeros = np.zeros((2, 3))  # [[0, 0, 0],[0, 0, 0,]]: Full 0
ones = np.ones((2, 3))  # [[1, 1, 1],[1, 1, 1,]]: Full 1
full = np.full((2, 3), 7)  # [[7, 7, 7],[7, 7, 7,]]: Full 7
arange = np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]

print(zeros)
print(ones)
print(full)
print(arange)

# Combine arrays
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

# Combine end-to-end (same row)
concat = np.concatenate((x, y))
print(concat)  # [1 2 3 4 5 6]

# Combine by rows (new row)
stacked = np.stack((x, y))
print(stacked)
# [[1 2 3]
#  [4 5 6]]

# Split arrays
split_example = np.array([0, 1, 2, 3, 4, 5, 6])
split_example_2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

# Split array to 3 part same size
split = np.array_split(split_example, 3)
for part in split:
    print(part)
# [0 1 2]
# [3 4]
# [5 6]

# Split 2D array
hsplit = np.hsplit(split_example_2, 2)
print(hsplit[0])
# [[1 2]
#  [5 6]]

# Search
search_example = np.array([10, 20, 30, 40, 50])
idx = np.where(search_example > 25)
print(idx)  # Get index: (array([2, 3, 4]),)
print(search_example[idx])  # Get value: [30 40 50]

# Sort
sort_example = np.array([3, 1, 5, 2, 4])
sorted_arr = np.sort(sort_example)
print(sorted_arr)

# Sort by columns
sort_matrix_example = np.array([[3, 2, 1], [6, 5, 4]])
print(np.sort(sort_matrix_example, axis=0))
# [[3 2 1]
#  [6 5 4]]
