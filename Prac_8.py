class stack:
    def __init__(self):
        self.elem=[]
        top=None
        #We use a list to form a stack whcih  have predefined functions like append and pop

    #push operation
    def push(self,element):
        self.elem.append(element)
        print('pushed')


    #pop function
    def pop(self):
        return self.elem.pop()


    def traversal(self):
        for i in self.elem:
            print(i)


s1=stack()

s1.push(1)
s1.push(2)
s1.push(3)
print("Printing the element")
s1.traversal()
s1.pop()
s1.pop()
print("Printing the element")
s1.traversal()