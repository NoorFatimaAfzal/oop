# Write a  Python program to create a class representing a stack data structure. Include methods for pushing, popping and displaying elements

class stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def is_empty(self):
        return len(self.items)==0
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Cant pop empty from empty stack! ")
    def display(self):
        print("Stack items: ",self.items)
    def remove(self,item):
        return self.items.remove(item)

stack1=stack()

stack1.push(10)
stack1.push(11)
stack1.push(12)
stack1.push("noor")

stack1.display()

popped_item = stack1.pop()
print("Popped item:", popped_item)

stack1.remove(10)
stack1.display()