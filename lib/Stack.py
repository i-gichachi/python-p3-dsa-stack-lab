class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = [] if items is None else items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            raise Exception("Stack is full")

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            raise Exception("Stack is empty")
    
    def size(self):
         return len(self.items)

    def full(self):
        return len(self.items) == self.limit

    def search(self, target):
        for index, item in enumerate(reversed(self.items)):
            if item == target:
                return len(self.items) - index - 1
        return -1