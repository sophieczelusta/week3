class MyQueue:

    def __init__(self,queue):
        self.que = queue

    def push(self,x):
        if len(self.que) <= 0:
            return "Queue is empty."
        else:
            if x not in self.que:
                print("Number not in queue.")
            else:
                self.que.remove(x)
                self.que.append(x)
                return self.que

    def pop(self):
        if len(self.que) <= 0:
            return "Queue is empty."
        else:
            first = self.que[1]
            self.que.remove(first)
            return first

    def peek(self):
        if len(self.que) <= 0:
            return "Queue is empty."
        else:
            return self.que[1]

    def empty(self):
        if len(self.que) <= 0:
            return True
        else:
            return False

lyst = [1,2,"b",4,5,6,"a",8,"c"]
length = len(lyst)
count = 0
for x in range(length - 2):
    if lyst[count] == str(lyst[count]):
        print("String in stack.")
        lyst.remove(lyst[count])
        count+=1
    else:
        count+=1

obj = MyQueue(lyst)
print(obj.push(4))
print(obj.pop())
print(obj.peek())
print(obj.empty())



class MyStack:
    def __init__(self,sta):
        self.stack = sta

    def push(self,x):
        if len(self.stack) <= 0:
            return "Stack is empty."
        else:
            if x not in self.stack:
                print("Number not in stack.")
            else:
                self.stack.remove(x)
                self.stack.append(x)
                return self.stack

    def pop(self):
        if len(self.stack) <= 0:
            return "Stack is empty."
        else:
            first = self.stack[len(self.stack) - 1]
            self.stack.remove(first)
            return first

    def top(self):
        if len(self.stack) <= 0:
            return "Stack is empty."
        else:
            return self.stack[len(self.stack) - 1]

    def empty(self):
        if len(self.stack) <= 0:
            return True
        else:
            return False

lyst = [1,2,"b",4,5,6,"a",8,"c"]
length = len(lyst)
count = 0
for x in range(length - 2):
    if lyst[count] == str(lyst[count]):
        print("String in stack.")
        lyst.remove(lyst[count])
        count+=1
    else:
        count+=1

obj = MyStack(lyst)
print(obj.push(4))
print(obj.pop())
print(obj.top())
print(obj.empty())
