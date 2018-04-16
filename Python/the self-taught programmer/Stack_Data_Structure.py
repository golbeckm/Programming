

class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        last_item = len(self.items)-1
        return self.items[last_item]

    def size(self):
        return len(self.items)

stack = Stack()

for letter in "Hello":
    stack.push(letter)

reverse = ""

for index in range(len(stack.items)):
    reverse += stack.pop()

print(reverse)
