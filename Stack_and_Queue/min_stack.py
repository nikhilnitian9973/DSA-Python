# leetcode 155
#T.C. = O(1) for every function

class Minstack():
    def __init__(self):
        self.stack  = []
    def push(self, val):
        if not self.stack:
            self.stack.append([val,val])
        else:
            self.stack.append([val,min(val,self.stack[-1][-1])])
    def pop(self):
        if not self.stack:
            return
        self.stack.pop()
    def top(self):
        return self.stack[-1][0]
    
    def minimum_ele(self):
        return self.stack[-1][-1]

a= Minstack()
a.push(2)
a.push(3)
print(a.top())
print(a.minimum_ele())
a.pop()
a.push(1)
print(a.top())
print(a.minimum_ele())
    