# Stack using list
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


# Example usage 
s = Stack()
s.push(10)
s.push(20)
s.push(30)


print("Top element : ", s.peek())             # Output: 30
print("Stack size : ", s.size())            # Output: 3

print("Popped : ", s.pop())             # Output: 30
print("Top after pop : ", s.peek())        # Output: 20
print("Is stack empty?", s.is_empty())

s.pop()
s.pop()
print("Is stack empty? ", s.is_empty())            # Output: True
print("Pop from empty stack : ", s.pop())














