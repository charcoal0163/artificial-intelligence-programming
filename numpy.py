# numpy
import numpy as np

# notice: to build a one-dimensional array, use 'array' method from numpy, add square brackets inside the parentheses to represent the first dimension
array = np.array([1, 2, 3])
print(array)
print(type(array))
print(array.size)
# notice: size is not a method, it's an attribute of the array, and it returns the number of elements in the array
print(array.ndim)
# notice: ndim attribute returns the dimension of the array
print(array.shape)
# notice: shape attribute returns the size of the array (rows and cols), and one-dimensional arrays always returns as (n,), where n is the number of elements
print(array.dtype)
# notice: dtype attribute returns the data type of the elements in the array

# notice: to build a two-dimensional array, add square brackets inside the square brackets inside the parentheses to represent the second dimension
array2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(array2)
print(type(array2))
print(array2.size)
print(array2.ndim)
print(array2.shape)
print(array2.dtype)

a = np.array([1, 2, 3])
b = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
print(b)

# notice: accessing an array uses index
print(a[1])
print(b[1])
# notice: b[1] returns the entire row since the column is not specified
print(b[0][-1])
print(b[1, 2])
# notice: to return a specific element in a two-dimensional array, specify the row first, then the column
print(b[:, 0])
# notice: to return the entire column, use the slicing method, where the row is taken as ':' which means 'all'
print(b[0:2, 1:3])
# notice: to return a section of the array, use the slicing method as well, which returns a two-dimensional array

# notice: an array is mutable, the values can be changed
b[2][3] = 8
print(b)

# notice: to build a three-dimensional array, add square brackets inside the square brackets inside the sqauare brackets inside the parentheses to represent the third dimension ('layers')
c = np.array([[[1, 2, 3, 4], [4, 3, 2, 1]], [[5, 6, 7, 8], [8, 7, 6, 5]], [[9, 8, 7, 6], [6, 7, 5, 4]]])
print(c)

# notice: to create an empty array of any dimension, use zeroes method and provide the shape of the array, and the shape can be user input or variables
x = np.zeros(5)
print(x)
y = np.zeros((3, 4))
print(y)

# notice: tp create an array full of 1's, use ones method and provide the shape of the array
e = np.ones(5)
print(e)
f = np.ones((3, 4))
print(f)

# notice: zeroes method always returns float, regardless of whether the inputted values are integers or not
grades = np.zeros(5)
for i in range(grades.size):
    grades[i] = input(f"Enter grade for student {i + 1}: ")
    
print(grades)

# notice: to cast the floating point values of the array into integers, use 'astype' method
marks = np.zeros(5)
for i in range(marks.size):
    marks[i] = input(f"Enter grade for student {i + 1}: ")
    
marks = marks.astype(int)
print(marks)

# element-wise operations: performing operations on two arrays
a1 = np.array([10, 20, 30])
a2 = np.array([5, 35, 25])

addition = a1 + a2
multiplication = a1 * a2
subtraction = a1 - a2
division = a1 / a2
floor = a1 // a2
modulus = a1 % a2

print(addition)
print(multiplication)
print(subtraction)
print(division)
print(floor)
print(modulus)

# array operations:
original = np.array([[2, 5], [6, 8]])
first = np.add(original, 5)
second = np.subtract(original, 5)
third = np.multiply(original, 2)
fourth = np.divide(original, 2)
fifth = np.mod(original, 2)
sixth = np.power(original, 2)

print(original)
print(first)
print(second)
print(third)
print(fourth)
print(fifth)
print(sixth)

# statistical operations:
med = np.median(original)
mean = np.mean(original)
standardDeviation = np.std(original)

print(med)
print(mean)
print(standardDeviation)

one = np.array([10, 5, 7, 90, 52, 43, 48])
sortOne = np.sort(one, )
print(sortOne)
# notice: to sort an array in ascending order, use sort method

highest = np.argmax(one)
print(highest)
# notice: argmax returns the position of the highest value of the array