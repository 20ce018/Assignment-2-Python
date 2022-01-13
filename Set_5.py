"""Convert tuple into list

first convert values of dictionary in list

set doesn't contain duplicate element
"""

list=[1,2,3,4,5,8,4,2,8,9,3,7,8,5,5]
listCount=[]
ExitAlready=False
for x in range(0,len(list)):
    for i in range(0,len(listCount)):
        if listCount[i][0]==list[x]:
            ExitAlready=True
            break
    if ExitAlready:
            ExitAlready=False
    else:
          listCount.append((list[x],list.count(list[x])))
        #Finding most common element
maxC,index=0,0
for i in range(0,len(listCount)):
    if listCount[i][1]>maxC:
        maxC=listCount[i][1]
        index=i
print("Frequently common element is:",listCount[index])