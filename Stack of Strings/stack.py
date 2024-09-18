class Stack:
    def __init__(self):
        self.data = []
    
    def push(self, item:str):
        if type(item) == str:
            self.data.append(str(item))
        else:
            return "can't push"
    
    def pop(self):
        if not self.is_empty():
            return self.data.pop()
        else:
            return "can't pop"
    
    def peek(self):
        if not self.is_empty():
            return self.data[-1]
        else:
            return "stack empty"
        
    def is_empty(self):
        if len(self.data) == 0:
            return True
        else:
            return False
        
    def __str__(self):
        return self.data
    

my_stack = Stack()
print(my_stack.is_empty())
print(my_stack.pop())
print(my_stack.push(1))
my_stack.push("hello")
my_stack.push("hi")
print(my_stack.peek())
print(my_stack.pop())
print(my_stack.__str__())