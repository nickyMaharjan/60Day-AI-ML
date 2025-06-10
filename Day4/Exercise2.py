import numpy as np

# arr = np.array([1,2,3,4,5],dtype='S')
#
# arr1 = np.array([1,2,3,4,5],ndmin=5)
#
# print(arr.ndim)
# print(np.__version__)
#
# print(type(arr))
#
# print(arr.dtype)
# print(arr1)

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
print("Original Array:\n", arr)

print("Sum:", np.sum(arr))

print("Mean:", np.mean(arr))

print("Transpose:\n", np.transpose(arr))

print("Element at [1][2]:", arr[1][2])  # Output: 6

print("First two rows:\n", arr[:2])

print("Array + 10:\n", arr + 10)


print("Second column:", arr[:, 1])

arr=[1,2,3,4]
np_arr=np.array(arr)
print(type(np_arr),np_arr)

