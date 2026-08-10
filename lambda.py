def add (x,y) :
    return x + y
def multi(x,y) :
    return x*y

print(add(10,5))
print(multi(10,5))

ad = lambda x,y : x + y    # lambda function can be used to create a function in less lines of code
mul = lambda x,y : x*y

print(ad(10,5),type(ad))
print(mul(10,5),type(mul))
