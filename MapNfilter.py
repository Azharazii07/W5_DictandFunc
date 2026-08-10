l1 = [8,9,10,11,12,13]
l2 = [7,8,9,10,11,10,14]

#l3 = l1 - l2  error , no such operation
dif = lambda x,y : x - y
l3 = map(dif,l1,l2)  # map takes each element of iterable -- passes it through function , returning results , lambda dif need two parameters
print(l3) # map object
print(list(l3))

inc = lambda a : a + 1
l4 = map(inc,l1)
print(l4) # map object
print(list(l4))

# filter function to eliminate
L = [ 4 , 9 , -81 , 49 , -100]

sqr = lambda a : (a**0.5) # square root

def isP (a) :    # checks positivity
    if a >= 0 :
        return a

sqL = map(sqr,(filter(isP,L)))
print(list(sqL))
