a=int(input())
b=list(map(int,input().split(' ')))
for i in b:
    c=b.count(i)
    if c==1:
        print(i)
        