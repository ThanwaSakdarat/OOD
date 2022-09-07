class Stack():
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    def push(self,a):
        self.items.append(a)
    def pop(self):
        return self.items.pop()
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)

def postFixeval(st):
    s = Stack()
    i = 0
    while i < len(st):
        c = st[i]
        
        if c in '+':
            p = float(s.pop()) 
            q = float(s.pop())
            a = p+q
            s.push(a)
        elif c in '-':
            p = float(s.pop())            
            q = float(s.pop())            
            a = q-p
            s.push(a)
        elif c in '*':
            p = float(s.pop()) 
            q = float(s.pop())
            a = p*q
            s.push(a)  
        elif c in '/':
            p = float(s.pop()) 
            q = float(s.pop())
            a = q/p
            s.push(a)            
        else:
            s.push(c)
        i += 1
    return s.pop()


print(" ***Postfix expression calcuation***")

token = list(input("Enter Postfix expression : ").split())



print("Answer : ",'{:.2f}'.format(postFixeval(token)))