import numpy as np

ar1 = input().strip().split(' ')
ar = np.array([int(i)
               for i in input().strip().split(' ')])
for i in range(1, int(ar1[0])):
    ar = np.vstack((ar, np.array([int(i)
                                  for i in input().strip().split(' ')])))

print(np.transpose(ar))
print(ar.flatten())

'''
arr1 = np.array([int(i) for i in ar1])
arr2 = np.array([int(i) for i in ar2])
arr3 = np.array([int(i) for i in ar3])

arr4 = np.array([arr2, arr3])
'''
