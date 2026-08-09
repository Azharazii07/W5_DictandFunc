import numpy as np
a1 = [1,2,3]
a2 = [4,2,-1]
a3 = [1,0,-1]

b1 = [3,-1,2]
b2 = [0,2,1]
b3 = [4,-1,-1]
A , B = [] , []
A.append(a1)
A.append(a2)
A.append(a3)

B.append(b1)
B.append(b2)
B.append(b3)

C = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(3) :
    for j in range(3) :
        for k in range(3) :
            C[i][j] += A[i][k]*B[k][j]
            
print(C[0],C[1],C[2],sep="\n")
X = np.asmatrix(A)
Y = np.asmatrix(B)
print(X*Y)

X = np.array(A)
Y = np.array(B)
print(X@Y)
