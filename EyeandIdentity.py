import numpy

# 3 is for  dimension 3 X 3
m, n = [int(i) for i in input().split(' ')]
print(numpy.eye(m, n))


print(str(numpy.eye(*map(int, input().split()))
          ).replace('1', ' 1').replace('0', ' 0'))
