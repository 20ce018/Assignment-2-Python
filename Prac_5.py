a=input()
str=""
for i in a:
    if i==i.upper():
        str+=i.lower()
    elif i ==i.lower():
        str+=i.upper()
    else:
        str+=i
print(str)