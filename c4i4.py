class Queue:
    def __init__(self,ls = None):
        if ls == None:
            self.items = []
        else:
            self.items = ls

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


info, action = input("Enter Input : ").split("/")

info = dict([i.split()[::-1] for i in info.split(',')])
lq = []

def search(id):
    for i in range(len(lq)):
        if info[lq[i].front()] == info[id]:
            return i
    return -1

for i in action.split(','):
    i = i.split()
    if i[0] == 'E':
        id = i[1]
        index = search(id)
        if index != -1 :
            lq[index].enQueue(id)
        else:
            lq.append(Queue([id]))


    elif i[0] == 'D':
        if not lq:
            print('Empty')
        else:
            print(lq[0].deQueue())
            if lq[0].isEmpty():
                lq.pop(0)