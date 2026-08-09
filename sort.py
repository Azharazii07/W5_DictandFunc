l = [-10 , 30 ,68 , 2 , 4, 1]

def sortl(m) :
    sl = []
    while(len(m)>0) :
        mini = l[0]
        for i in range(len(l)) :
            if l[i] < mini :
                mini = l[i]
        l.remove(mini)
        sl.append(mini)
        
    return sl
    
print(f"Sorted list is {sortl(l)}")
        
l = [-10 , 30 ,68 , 2 , 4, 1]

def mini(n) :
    mini = n[0]
    for x in n :
        if x < mini :
            mini = x
    return mini

def sortl1(m) :
    sl = []
    while(len(m)>0) :
        minim = mini(l)
        m.remove(minim)
        sl.append(minim)
    return sl
print(f"Sorted list is {sortl1(l)}")
