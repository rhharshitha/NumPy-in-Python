import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

print("Original Array:", arr)

# Accessing elements
print("First Element:", arr[0])
print("Third Element:", arr[2])

# Slicing array
print("First Three Elements:", arr[0:3])
print("Last Three Elements:", arr[3:6])

# Changing an element
arr[1] = 100
print("Updated Array:", arr)
