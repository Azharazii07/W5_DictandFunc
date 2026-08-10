l = ["a","e","i","o","u"]

for i in range(len(l)) :
    print(i, l[i]) 

# Enumerate is to couple an element in a indexable collection with its index

for i in enumerate(l) :
    print(3,i)

# zip function is to couple two lists , not index and element

m = [3,8,5,1,7]

print(zip(l,m)) # zip object
print(list(zip(l,m)))     # correspondants -- list of tuples
print(dict(zip(l,m)))     # correspondants -- dictionary
