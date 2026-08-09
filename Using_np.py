import numpy as np
a = b = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
A = np.asmatrix(a)
B = np.asmatrix(b)
C = A@B
print(C[0],C[1],C[2],C[3],sep="\n")
