import numpy
lst = [int(i) for i in input().split(' ')]

# Default type is float
print(numpy.zeros(lst, dtype=numpy.int))
# Output : [[ 0.  0.]]

# Type changes to int
print(numpy.ones(lst, dtype=numpy.int))
# Output : [[0 0]]
