#1
import numpy as np

#2
print(np.__version__)
np.show_config()

#3
nullvector = np.zeros(10)
print(nullvector)

#4
nullvector = np.zeros((10, 10))
print("%d bytes" %(nullvector.size * nullvector.itemsize))

#6
nullvector = np.zeros(10)
nullvector[4] = 1
print(nullvector)

#7
nullvector = np.arange(10, 50)
print(nullvector)


#9
nullvector = np.arange(0,9).reshape(3,3)
print(nullvector)

#15 Create a 2d array with 1 on the border and 0 inside 경계는1 내부는 0
nullvector = np.ones((10,10))
nullvector[1:-1,1:-1] = 0
print(nullvector)

