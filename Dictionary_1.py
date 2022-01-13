dist={'Bhargavi':1,'Harshit':2,'Drash':3,'Bansi':4}
def present_key(x):
    if x in dist:
        print("Key is present in dictionary")
    else:
        print("Key is not present in dictionary")

present_key('Bhargavi')#Bhargavi is already present in dictionary
present_key('Aesha')#Aesha is  not present in dectionary