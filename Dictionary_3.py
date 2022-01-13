def returnSum(myDict):#Function to sum all item
    list=[]
    for i in myDict:#For loop
        list.append(myDict[i])
    final=sum(list)
    return final

dict={'x':100,'y':200,'z':300,'h':400}
print("The sum is: ",returnSum(dict))