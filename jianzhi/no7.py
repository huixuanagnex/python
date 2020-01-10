"""
用两个栈实现队列
"""
class myqueue():
    def __init__(self):
        self.stackA = []
        self.stackB = []
    def push(self,x):
        self.stackA.append(x)

    def pop(self):
        if not self.stackB:
            while self.stackA:
                self.stackB.append(self.stackA.pop())
        return self.stackB.pop()


    def peek(self):
        if not self.stackB:
            while self.stackA:
                self.stackB.append(self.stackA.pop())
        return self.stackB[-1]

    def empty(self):
        return len(self.stackA)==0 and len(self.stackB)==0

obj = myqueue()
obj.push("a")
obj.push("b")
obj.push("c")
print("pop:"+obj.pop())
print("peek:"+obj.peek())
print("empty"+str(obj.empty()))
obj.pop()
obj.pop()
print("empty"+str(obj.empty()))






