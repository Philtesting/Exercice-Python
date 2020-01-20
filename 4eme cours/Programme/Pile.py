class Stack:

    def __init__(self):
        self.stack = []

    def add(self, dataval):
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False
    def peek(self):     
	    return self.stack[0]

    def remove(self):
        if len(self.stack) <= 0:
            return ("No element in the Stack")
        else:
            return self.stack.pop()

pile = Stack()
pile.add(1)
pile.add(2)
print(pile.peek())
pile.add(3)
pile.add(4)
print(pile.remove())
