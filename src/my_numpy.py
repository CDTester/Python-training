import numpy as np

"""
NumPy is a Python library used for working with arrays.
It also has functions for working in domain of linear algebra, fourier transform, and matrices.
NumPy stands for Numerical Python.
In Python we have lists that serve the purpose of arrays, but they are slow to process.
NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.
The array object in NumPy is called ndarray, it provides a lot of supporting functions that make
working with ndarray very easy.
Arrays are very frequently used in data science, where speed and resources are very important.
Data Science is a branch of computer science where we study how to store, use and analyze data for 
deriving information from it.
"""

arr = np.array([1, 2, 3, 4, 5])
print("arr np.array([1, 2, 3, 4, 5]) =", arr)
print("Get the 3rd element:", arr[2])
print(type(arr))

tup = np.array((1, 2, 3, 4, 5))
print("\ntup np.array((1, 2, 3, 4, 5)) =", tup)
print("Get the 3rd element:", tup[2])
print(type(tup))

arr_0D = np.array(42)
print("\narr_0D np.array(42) =", arr_0D)
print("Get the 1st element:", arr_0D)
print("number of dimensions of arr_0D is:", arr_0D.ndim)
print("Shape of arr_0D:", arr_0D.shape)

arr_1D = np.array([1, 2, 3, 4, 5, 6, 7])
print("\narr_1D np.array([1, 2, 3, 4, 5, 6, 7]) =", arr_1D)
print("Get the 1st element:", arr_1D[0])
print("number of dimensions of arr_1D is:", arr_1D.ndim)
print("Shape of arr_1D:", arr_1D.shape)

arr_2D = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]])
print("\narr_2D np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]]) =\n", arr_2D)
print('2nd element on 1st row: ', arr_2D[0, 1])
print('last element on 2nd row: ', arr_2D[1, -1])
print("number of dimensions of arr_2D is:", arr_2D.ndim)
print("Shape of arr_2D:", arr_2D.shape)

arr_3D = np.array([ [ [1, 2, 3], [4, 5, 6] ], [ [11, 12, 13], [14, 15, 16] ] ], ndmin=3, ndmax=5)
print("\narr_3D np.array([[[1, 2, 3], [4, 5, 6]], [[11, 12, 13], [14, 15, 16]]], ndmin=3, ndmax=5) =\n", arr_3D)
print('3rd element on 1st row of the 2nd matrix: ', arr_3D[1, 0, 2])
print("number of dimensions of arr_3D is:", arr_3D.ndim)
print("Shape of arr_3D:", arr_3D.shape)


print("\narr_1D =", arr_1D)
print("Slicing - get the 2nd and 3rd elements of the 1st row of arr_1D: ", arr_1D[1:3])
print("Slicing - get all elements from the 2nd element to the end of arr_1D: ", arr_1D[1:])
print("Slicing - get all elements up to the 3rd element of arr_1D: ", arr_1D[:3])
print("slicing - get last 3 elements of arr_1D: ", arr_1D[-3:])
print("Step - return every other element from the 2nd to the 5th element of arr_1D: ", arr_1D[1:5:2])

print("\narr_2D =", arr_2D)
print("Slicing - get the 2nd to 4th elements of the 2nd row of arr_2D: ", arr_2D[1, 1:4])
print("Slicing - get the 3rd element from both rows of arr_2D: ", arr_2D[0:2, 2])

arr_long = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print("\narr_long np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) =", arr_long)
newarr = arr_long.reshape(4, 3)
print("reshaped:  arr_long.reshape(4, 3) =\n", newarr)
flattened = newarr.reshape(-1)
print("flattened: newarr.reshape(-1) =", flattened)


"""
NumPy has some extra data types, and refer to data types with one character, 
like i for integers, u for unsigned integers etc.
Below is a list of all data types in NumPy and the characters used to represent them.

i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
"""

print("\narr_1D =", arr_1D)
print("Get the data type of arr_1D:", arr_1D.dtype)

arr_fruit = np.array(['apple', 'banana', 'cherry'])
print("\narr_fruit =", arr_fruit)
print("Get the data type of arr_fruit:", arr_fruit.dtype)

arr_intStr = np.array([1, 2, 3, 4], dtype='S')
print("\narr_intStr np.array([1, 2, 3, 4], dtype='S') =", arr_intStr)
print("Get the data type of arr_intStr:", arr_intStr.dtype)

arr_int = np.array([1, 2, 3, 4], dtype='i4')
print("\narr_int =", arr_int)
print("Get the data type of arr_int:", arr_int.dtype)

print("\nCopy array as another type:")
arr_float = arr_int.astype('f4')
print("arr_float from arr_int =", arr_float)
print("Get the data type of arr_float:", arr_float.dtype)

arr_int2 = np.array([0, 1, 2, 3])
x = arr_int2.view()
print("\narr_int2 =", arr_int2)
newarr = arr_int2.astype(bool)
print("newarr =", newarr)
print("Get the data type of newarr:", newarr.dtype)

print("\nIterating:")

arr2_1d = np.array([1, 2, 3])
print("arr2_1d =", arr2_1d) 
for element in arr2_1d:
  print(element)

arr_2D = np.array([[1, 2, 3], [4, 5, 6]])
print("\narr_2D =", arr_2D)
for row in arr_2D:
  print(row)
  for element in row:
    print(element)

print("\nIterating is done with nditer():")
for element in np.nditer(arr_2D):
    print(element)


"""
JOIN
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
arr2 = np.stack((arr1, arr2), axis=1)
arr3 = np.hstack((arr1, arr2))
arr4 = np.vstack((arr1, arr2))
arr5 = np.dstack((arr1, arr2))
print(arr) # = [1 2 3 4 5 6]
print(arr2) # = [[1 4], [2 5], [3 6]]
print(arr3) # = [1 2 3 4 5 6]
print(arr4) # = [[1 2 3], [4 5 6]]
print(arr5) # = [[1 4], [2 5], [3 6]]

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print(arr) # = [[1 2 5 6], [3 4 7 8]]


SPLIT
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr) # = [array([1, 2]), array([3, 4]), array([5, 6])]

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print(newarr) # = [array([[ 1,  2], [ 3,  4]]), array([[ 5,  6], [ 7,  8]]), array([[ 9, 10], [11, 12]])]


SEARCH
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x) # = (array([3, 5, 6]),) - returns the indices where the condition is true


SORT
arr = np.array([3, 2, 0, 1])
print(np.sort(arr)) # = [0 1 2 3] - returns a sorted copy of the array, does not change the original array


FILTER
arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
print(newarr) # = [41 43] - returns the elements from the array where the corresponding boolean value is True

arr = np.array([41, 42, 43, 44])
filter_arr = arr > 42
newarr = arr[filter_arr]
print(filter_arr) # = [False False True True] - returns a boolean array where the condition is true
print(newarr) # = [43 44] - returns the elements from the array where the corresponding boolean value is True

"""