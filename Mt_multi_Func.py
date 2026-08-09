# 1. Intialization of a null matrix
# 2. Dot product of two lists
# 3. selecting i-th row and j-th column

def ini(dim) : # intilization of product C
    L = []
    for i in range(dim) :
        l = []
        for j in range(dim) :
            l.append(0)
        L.append(l)
    return L
    
def dprod(x,y): # dot product of two list
    ans = 0
    for i in range(len(x)) :
        ans += x[i]*y[i]
    return ans

def row(M,r) : # selects ith row
    l = []
    for x in range(len(M)) :
        l.append(M[r][x])
    return l

def col(M,c) : # selects jth row
    l = []
    for x in range(len(M)) :
        l.append(M[x][c])
    return l

def Mt_Mul(A,B) :
    C = ini(len(A))
    for i in range(len(B)) :
        for j in range(len(C)) :
            x = row(A,i)
            y = col(B,j)
            C[i][j] = dprod(x,y)
    return C
# a , b = [[2,4],[3,4]] , [[1,1],[0,0]] 
#a = [[1,2,3],[4,2,-1],[1,0,-1]]
#b = [[3,-1,2],[0,2,1],[4,-1,-1]]
a = b = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
