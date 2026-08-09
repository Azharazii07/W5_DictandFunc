def UC(s) :
    ct = 0
    for x in s :
        if x.isupper() :
            ct += 1
    return ct

def LC(s) :
    ct = 0
    for x in s :
        if x.islower() :
            ct += 1
    return ct
    
def Char(s) :
    ct = 0
    for x in s :
        ct += 1
    return ct
    
def Words(s) :
    ct = 0
    for x in s.split() :
        ct += 1
    return ct
    
st = input("Enter a string\n")
print(UC(st),LC(st),Char(st),Words(st))
