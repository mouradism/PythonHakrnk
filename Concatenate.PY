
import numpy as np
ar1 = input().strip().split(' ')

for i in range(0, int(ar1[0])+int(ar1[0])):
    ar = np.vstack((ar, np.array([int(i)
                                  for i in input().strip().split(' ')])))

print(ar)

'''
import numpy

array_1 = numpy.array([[1, 2, 3], [0, 0, 0]])
print(array_1)
array_2 = numpy.array([[0, 0, 0], [7, 8, 9]])
array_1 = numpy.concatenate((array_1, array_2))
print(array_1)
'''
