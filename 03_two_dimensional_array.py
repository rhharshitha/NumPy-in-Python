import numpy as np

# Creating a 2D array
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print("Two Dimensional Array:")
print(arr)

print("Number of Rows and Columns:", arr.shape)
print("First Row:", arr[0])
print("Second Row:", arr[1])

# Expected Output:
# Two Dimensional Array:
# [[1 2 3]
#  [4 5 6]]
# Number of Rows and Columns: (2, 3)
# First Row: [1 2 3]
# Second Row: [4 5 6]
