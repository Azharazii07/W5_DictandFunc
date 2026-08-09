import sys
def CP(r) :
    peri = (2*22*r)//7
    return peri

def CA(r) :
    area = (22*r*r)//7
    return area
    
def RP(l,b) :
    peri = 2*(l+b)
    return peri
    
def RA(l,b) :
    area = l*b
    return area
    
sp =  input("enter shape\n") 
if sp == "exit" :
    sys.exit("Stop execution")
op = input("enter operator\n")
    
if sp == "Circle" :
    rad = int(input("Enter radius\n"))
    if op == "Area" :
        print(f"{CA(rad)} sq. units")
    elif op == "Perimeter" :
        print(f"{CP(rad)} units")
elif sp == "Rectangle" :
    l = int(input("Enter length\n"))
    b = int(input("Enter breadth\n"))
    if op == "Area" :
        print(f"{RA(l,b)} sq. units")
    elif op == "Perimeter" :
        print(f"{RP(l,b)} units")
