class MyStack(object):

    def __init__(self):
        self.qu = deque()
        

    def push(self, x):
        self.qu.append(x)
        for _ in range(len(self.qu)-1):
            self.qu.append(self.qu.popleft())
        

    def pop(self):
        return self.qu.popleft()
        

    def top(self):
        return self.qu[0]
        

    def empty(self):
        return len(self.qu) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()