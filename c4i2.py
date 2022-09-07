
class Queue:
    def __init__(self):
        self.items = []

    def push(self, i):
        self.items.append(i)

    def pop(self):
        return self.items.pop(0)

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def front(self) :
            return self.items[0] 
Q = Queue()
q1  = Queue()
q2  = Queue()
n1,n2 = input("Enter people and time : ").split()
for i in n1 : 
    Q.push(i)
    
p = 0
p1 = 0
p2 = 0
while(1):
    p += 1
    if q1.size() < 5:
        if not Q.isEmpty():
            q1.push(Q.front())
            Q.pop()
    else :
       if not Q.isEmpty():
            q2.push(Q.front())
            Q.pop()
    print(f'{str(p)} {Q.items} {q1.items} {q2.items}')

    if not q1.isEmpty():
        p1 += 1
    if not q2.isEmpty():

        p2 += 1  
    if p1 == 3 :
        q1.pop()
        p1 = 0

    if p2 == 2 :
        q2.pop()
        p2 = 0
    if p == int(n2) :
        break