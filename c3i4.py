class Stack:
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
    def peek(self):
        return self.items[-1]

S = Stack()


inp = input('Enter Input : ').split(',')
for i in range(len(inp)):
    x = inp[i].split()     
    if x[0]=='A':
        if S.isEmpty():
            S.push(int(x[1]))
        else:
            while not S.isEmpty() and int(x[1]) >= S.peek():
                S.pop()
            S.push(int(x[1]))
    else:print(S.size())

