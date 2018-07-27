class MyQueue:

    def __init__(self,queue):
        self.que = queue

    def push(self,x):
        if len(self.que) <= 0 and len(self.que[0]) <= 0 and len(self.que[1]) <= 0:
            return "Queue is empty."
        else:
            if x not in self.que:
                print("Number not in queue.")
            else:
                self.que.remove(x)
                self.que.append(x)
                return self.que

    def pop(self):
        if len(self.que) <= 0 and len(self.que[0]) <= 0 and len(self.que[1]) <= 0:
            return "Queue is empty."
        else:
            first = self.que[1]
            self.que.remove(first)
            return first

    def peek(self):
        if len(self.que) <= 0 and len(self.que[0]) <= 0 and len(self.que[1]) <= 0:
            return "Queue is empty."
        else:
            return self.que[1]

    def empty(self):
        if len(self.que) <= 0 and len(self.que[0]) <= 0 and len(self.que[1]) <= 0:
            return True
        else:
            return False



stack1 = [1,3,5,7,9,"op"]
length = len(stack1)
count = 0
for x in range(length - 2):
    if stack1[count] == str(stack1[count]):
        print("String in stack.")
        stack1.remove(stack1[count])
        count+=1
    else:
        count+=1

stack2 = [1,2,"b",4,5,6,"a",8,"c"]
length = len(stack2)
count = 0
for x in range(length - 2):
    if stack2[count] == str(stack2[count]):
        print("String in stack.")
        stack2.remove(stack2[count])
        count+=1
    else:
        count+=1

obj = MyQueue([stack1,stack2])
obj.emp()
