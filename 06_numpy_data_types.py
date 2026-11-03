import numpy as np

# Creating arrays with different data types
a = np.array([10, 20, 30], dtype=int)
b = np.array([1.5, 2.5, 3.5], dtype=float)
c = np.array([True, False, True], dtype=bool)

print("Integer Array:", a)
print("Integer Data Type:", a.dtype)

print("Float Array:", b)
print("Float Data Type:", b.dtype)

print("Boolean Array:", c)
print("Boolean Data Type:", c.dtype)
