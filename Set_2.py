def removeele(element): #Function to remove an item from set
    if element in A:#for loop
        A.discard(element)#discard used to remove that element
        return A
    else:
        return 'Not exist in set'

A=set([1,2,3])
print(removeele(1))
print(removeele(100))
