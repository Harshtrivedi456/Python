import numpy as np
list1 = [2, 4, 6, 8]
array1 = np.array(list1)
print(array1)

import numpy as np
array1 = np.array([2, 4, 6, 8])
print(array1)

#np.zeros exp
import numpy as np
array1 = np.zeros(4)
print(array1)

#np.arrange()
import numpy as np
# create an array with values from 0 to 4
array1 = np.arange(5)
print("Using np.arange(5):", array1)
# create an array with values from 1 to 8 with a step of 2
array2 = np.arange(1, 9, 2)
print("Using np.arange(1, 9, 2):",array2)

#np.random.rand()

import numpy as np
# generate an array of 5 random numbers
array1 = np.random.rand(5)
print(array1)


#Task
import numpy as np
# Example 1: Creation of 1D array
arr1=np.array([10,20,30])
print("My 1D array:\n",arr1)

# Example 2: Create a 2D numpy array
import numpy as np
arr2 = np.array([[10,20,30],[40,50,60]])
print("My 2D numpy array:\n", arr2)

# Example 3: Create a sequence of integers
# from 0 to 20 with steps of 3
import numpy as np
n=int(input('ENTER LOWER '))
m=int(input('ENTER UPPER '))
s=int(input('ENTER steps '))
arr= np.arange(n, m, 3)
print ("A sequential array with steps of ",s,":\n", arr)

# Example 4: Create a sequence of 5 values in range 0 to 3
import numpy as np
arr= np.linspace(0, 3, 5)
print ("A sequential array with 5 values between 0 and 5:\n", arr)

# Example 8: Use ones() create array
import numpy as np
arr = np.ones((2,3))
print("numpy array:\n", arr)
print("Type:", type(arr))

 

#Creating NumPy Arrays With a Defined Data Type
import numpy as np
# create an array of 8-bit integers
array1 = np.array([1, 3, 7], dtype='int8')
# create an array of unsigned 16-bit integers
array2 = np.array([2, 4, 6], dtype='uint16')
# create an array of 32-bit floating-point numbers
array3 = np.array([1.2, 2.3, 3.4], dtype='float32')
# create an array of 64-bit complex numbers
array4 = np.array([1+2j, 2+3j, 3+4j], dtype='complex64')
# print the arrays and their data types
print(array1, array1.dtype)
print(array2, array2.dtype)
print(array3, array3.dtype)
print(array4, array4.dtype)

#NumPy Type Conversion
import numpy as np
# create an array of integers
int_array = np.array([1, 3, 5, 7])
# convert data type of int_array to float
float_array = int_array.astype('float')
# print the arrays and their data types
print(int_array, int_array.dtype)
print(float_array, float_array.dtype)

#NumPy Array Attributes

# Attributes	Description
# ndim	returns number of dimension of the array
# size	returns number of elements in the array
# dtype	returns data type of elements in the array
# shape	returns the size of the array in each dimension.
# itemsize	returns the size (in bytes) of each elements in the array
# data	returns the buffer containing actual elements of the array in memory

import numpy as np
# create a 2-D array 
array1 = np.array([[2, 4, 6],
                  [1, 3, 5]])
# check the dimension of array1
print('Dimensio of array is ',array1.ndim,'D')

import numpy as np
array1 = np.array([[1, 2, 3],
                 [6, 7, 8]])
# return total number of elements in array1
print('Size of the array is ',array1.size)

import numpy as np
array1 = np.array([[1, 2, 3],
                [6, 7, 8]])
# return a tuple that gives size of array in each dimension
print('Shape of the array is ',array1.shape)

import numpy as np
# create an array of integers 
array1 = np.array([6, 7, 8])
# check the data type of array1
print('Data type of the array is ',array1.dtype)

import numpy as np
# create a default 1-D array of integers
array1 = np.array([6, 7, 8, 10, 13])
# create a 1-D array of 32-bit integers 
array2 = np.array([6, 7, 8, 10, 13], dtype=np.int32)
# use of itemsize to determine size of each array element of array1 and array2
print('Size of the first array is ',array1.itemsize)  # prints 8
print('Size of the second array is ',array2.itemsize)  # prints 4


import numpy as np
array1 = np.array([6, 7, 8])
array2 = np.array([[1, 2, 3],
                   	    [6, 7, 8]])
# print memory address of array1's and array2's data
print("\nData of array1 is: ",array1.data)
print("Data of array2 is: ",array2.data)

#Multiplication of two given matrixes
import numpy as np
p = [[1, 0], [0, 1]]
q = [[1, 2], [3, 4]]
print("Original matrices:")
print(p)
print(q)
# Perform matrix multiplication using np.dot
result1 = np.dot(p, q)
print("Result of the matrix multiplication:")
print(result1)

#Multiplication of two given matrixes
import numpy as np
p = [[1, 0], [0, 1]]
q = [[1, 2], [3, 4]]
print("Original matrices:")
print(p)
print(q)
# Perform matrix multiplication using np.dot
result1 = np.matmul(p, q)
print("Result of the matrix multiplication:")
print(result1)

#addition of matrices
import numpy as np
a=[[1,2,3],[4,5,6]]
b=[[7,8,9],[1,2,1]]
c=np.add(a,b)
print(c)

#Compute the determinant of a given square array.
import numpy as np
from numpy import linalg as LA
a = np.array([[1, 0], [1, 2]])
# Display the original 2x2 array 'a'
print("Original 2-d array")
print(a)
print("Determinant of the said 2-D array:")
print(np.linalg.det(a))


def add(a,b)
    return a+b
    