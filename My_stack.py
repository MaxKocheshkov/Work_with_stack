# Task 1
class Stack:

    def __init__(self):
        self.my_stack = []

    def isEmpty(self):
        return self.my_stack == []

    def push(self, item):
        self.my_stack.append(item)

    def pop(self):
        return self.my_stack.pop()

    def peek(self):
        return self.my_stack[len(self.my_stack) - 1]

    def size(self):
        return len(self.my_stack)


test_stack = Stack()
print(test_stack.isEmpty())
test_stack.push('dfsafag')
print(test_stack.isEmpty())
print(test_stack.peek())
print(test_stack.size())



