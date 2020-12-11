import numpy


my_array = [float(i) for i in input().split(' ')]
print(str(numpy.floor(my_array)).replace('.', '. ').replace(
    '[', '[ ').replace(' ]', ']'))  # [ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
print(str(numpy.ceil(my_array)).replace('.', '. ').replace(
    '[', '[ ').replace(' ]', ']'))  # [  2.   3.   4.   5.   6.   7.   8.   9.  10.]
print(str(numpy.rint(my_array)).replace('.', '. ').replace(
    '[', '[ ').replace(' ]', ']'))  # [  1.   2.   3.   4.   6.   7.   8.   9.  10.]
