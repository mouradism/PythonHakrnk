import numpy
ar0 = input().strip().split(' ')
a = numpy.array([int(i)
                 for i in input().strip().split(' ')])
for i in range(1, int(ar0[0])):
    a = numpy.vstack((a, numpy.array([int(i)
                                      for i in input().strip().split(' ')])))
b = numpy.array([int(i)
                 for i in input().strip().split(' ')])
for i in range(1, int(ar0[0])):
    b = numpy.vstack((b, numpy.array([int(i)
                                      for i in input().strip().split(' ')])))


# print(a + b)  # [  6.   8.  10.  12.]
addd = numpy.add(a, b)
addd.shape = (int(ar0[0]), int(ar0[1]))
print(addd)  # [  6.   8.  10.  12.]

# print(a - b)  # [-4. -4. -4. -4.]
souss = numpy.subtract(a, b)
souss.shape = (int(ar0[0]), int(ar0[1]))
print(souss)  # [-4. -4. -4. -4.]

# print(a * b)  # [  5.  12.  21.  32.]
multp = numpy.multiply(a, b)
multp.shape = (int(ar0[0]), int(ar0[1]))
print(multp)  # [  5.  12.  21.  32.]

# print(a / b)  # [ 0.2         0.33333333  0.42857143  0.5       ]
# [ 0.2         0.33333333  0.42857143  0.5
floor = numpy.floor_divide(a, b)
floor.shape = (int(ar0[0]), int(ar0[1]))
print(floor)

# print(a % b)  # [ 1.  2.  3.  4.]
mdd = numpy.mod(a, b)
mdd.shape = (int(ar0[0]), int(ar0[1]))
print(mdd)  # [ 1.  2.  3.  4.]

# [  1.00000000e+00   6.40000000e+01   2.18700000e+03   6.55360000e+04]
# print(a**b)
# [  1.00000000e+00   6.40000000e+01   2.18700000e+03   6.55360000e+04]
pwr = numpy.power(a, b)
pwr.shape = (int(ar0[0]), int(ar0[1]))
print(pwr)
