import numpy as np

"""
# EX 1

A = np.array([1,5,7,8])
B = np.array([1,2,3,4,5,6,7,8,9])
C = np.zeros(10)
D = np.zeros([2,5])
E = np.ones(10)
F = np.ones([2,5])
G = np.array([8.5]* 10)
H = np.array(range(1,10))
I = np.array(range(1,10)).reshape(3,3)
J = np.eye(4)
K = np.random.standard_normal()
L = np.random.randint(1, 11, 20)
m = L.reshape(4,5)
N = np.random.randn(0, 1, 7)
O = np.linspace(0, 1, 5)

#print(M)

# EX 2

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(a.shape)
print(a.shape)
print(a.size)
print(a.dtype)

"""

#EX 3

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
"""
print(a[1,1])
a[1][1] = 0
print(a[:,-1])

A = np.random.randint(0, 10, 12).reshape(4,3)
print(A)

B = np.any(A < 5)
print(B)

A = np.where(A < 5, 0, A)
print(A)
"""

#EX 4

#1
A = np.random.randint(0, 10, 12).reshape(4,3)
print(A)

#2
print(A.shape)

#3
A = A.astype(np.float32)

#4
A[-1, -1] = 3
print(A) #mais ca na pas 1 dimension ...

#5



