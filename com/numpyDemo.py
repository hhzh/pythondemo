import numpy as np

# from numpy import *
#
# result = random.rand(4, 4)
# print(result)
#
# randMat = mat(result)
# print(randMat)
# print(randMat)


a = np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 5])
c = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]])

# print(a)
# print(a * b)
# print(b.dtype)
# print(b.shape)
print(c)
print(c.dtype, c.shape)
c.shape = 4, 3
print(c)
c[1] = 100
print(c)

print(np.arange(0, 1, 0.1, dtype="float32"))
