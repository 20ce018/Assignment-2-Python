dict1={1:10,2:20}
dict2={3:30,4:40}
dict3={5:50,6:60}
dict4={}#empty dictionary
for i in(dict1,dict2,dict3):#For loop
   # print("i",i)
    dict4.update(i)#update with all i values
print(dict4)