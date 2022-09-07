
class Queue:
    def __init__(self):
        self.items = []

    def enQueue(self, i):
        self.items.append(i)

    def deQueue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def front(self) :
            return self.items[0]  

Q = Queue()
l1 , l2 = input("Enter Input : ").split("/")

for i in l1.split():
    Q.enQueue(i)

for i in l2.split(',') : 
    i = i.split()
    if i[0] == 'E':
        Q.enQueue(i[1])

    elif i[0] == 'D':
        if not Q.isEmpty():
            Q.deQueue()

cl = []
while not Q.isEmpty():
    d = Q.deQueue()
    if d in cl:
        print('Duplicate')
        exit()
    else:
        cl.append(d)
print('NO Duplicate')
