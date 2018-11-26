import numpy as np
numbers = np.array(range(1, 11), copy = True)
print(numbers)

ones = np.ones([2, 4], dtype= np.float64)
print(ones)

zeros = np.zeros([2, 4], dtype = np.float64)
print(zeros)

empty = np.empty([2, 4], dtype = np.float64)
print(empty)

eye = np.eye(3)
print(eye)

np_numbers = np.arange(2, 5, 0.25)
print(np_numbers)