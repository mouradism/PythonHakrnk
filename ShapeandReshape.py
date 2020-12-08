import numpy

arr = input().strip().split(' ')
my_1D_array = numpy.array([int(i) for i in arr])
my_1D_array.shape = (3, 3)
print(my_1D_array)
'''
my_2D_array = numpy.array([[1, 2], [3, 4], [6, 5]])
print(my_2D_array.shape)  # (3, 2) -> 3 rows and 2 columns
'''
