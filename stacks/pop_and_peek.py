"""
Complete the peek method. It should return the top item from the stack without
modifying the stack. If the stack is empty, return None.
Complete the pop method. It should remove and return the top item from the
stack. If the stack is empty, return None.
"""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]

    def pop(self):
        if len(self.items) == 0:
            return None
        item = self.items[-1]
        del self.items[-1]
        return item


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

print(stack.peek())
print(stack.pop())
