import numpy as np


def arrays(arr):
    for i, a in enumerate(arr):
        arr[i] = float(a)
        print(i)
    arr = np.array(arr)
    # complete this function
    # use numpy.array
    return np.flip(arr)


arr = "1 2 3 4 -8 -10".strip().split(' ')

result = arrays(arr)
print(result)
