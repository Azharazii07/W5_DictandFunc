'''Quick Shortcut :
Find the two smaller numbers and add them.Compare that sum to the largest number.If Sum of small sides > Largest side, it works '''
def dt(x,y) :
    a = x[0] - y[0]
    b = x[1] - y[1]
    dist = (a**2 + b**2)**0.5
    return dist

def Sortls(a,b,c) :
    l = [a,b,c]
    return sorted(l)
    
def verdict(l) :
    return "Triangle" if (l[0] + l[1] > l[2]) else "Not a Triangle"
L = [[0,0],[0,0],[0,0]]
nL = []
for i in range (3) :
    for j in range (2) :
        print("for", i , j)
        L[i][j] = float(input())
    T = tuple(L[i])
    nL.append(T)
print(nL)
        
A = dt(L[0],L[1])
B = dt(L[1],L[2])
C = dt(L[2],L[0])

distL = Sortls(A,B,C)
print(distL)
print(verdict(distL))
        
    

    


    
