import numpy as np

np.random.seed(5)
array = np.random.randint(1, 100, 9)
print("Original array:", array)
print("Square roots:", np.sqrt(array))
print("Number of dimensions:", array.ndim)

new_array = array.reshape(3, 3)
print("\nReshaped 3 x 3 array:\n", new_array)
print("Dimensions after reshape:", new_array.ndim)
print("\nFlattened array:", new_array.ravel())
print("\nLast row, columns 2 and 3:", new_array[2, 1:3])
print("\nRows 2 to 3:\n", new_array[1:3])
print("\nFirst column:\n", new_array[:, 0:1])
