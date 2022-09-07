class Queue:
    def __init__(self,list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    def enQueue(self,i):
        self.items.append(i)
    def deQueue(self):
        return self.items.pop(0)
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
S = Queue()
inp = list(input("Enter Input : ").split(','))
for i in range(len(inp)):
    x = inp[i].split()     
    if x[0]=='E':
        S.enQueue(x[1])
        print("Add",x[1],"index is",int(S.size()-1))
    elif x[0] =='D':
        if not S.isEmpty():
            print("Pop",S.deQueue(),"size in queue is",S.size())
        else:
            print("-1")

if int(S.size())>0:
    print("Number in Queue is : ", S.items)
else:
    print("Empty")
