class Stack():
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    def push(self,i):
        self.items.append(i)
    def pop(self):
        return self.items.pop()
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)

s = list(input("Enter : ").split())
a = Stack()
i = 0 
j = 0 
while i < len(s):
    c = s[i]
    a.push(c)
    i += 1
print("the size", a.size())

while not a.size() == 0:
    print(a.pop())