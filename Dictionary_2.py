dict1={1:10,2:20,3:30,4:40}
dict2={'a':6,'b':9,'c':11,'d':99}
def merge(dict1,dict2):#Function to merge 2  dictionary
    return (dict1.update(dict2))
merge(dict1,dict2)

print(dict1)