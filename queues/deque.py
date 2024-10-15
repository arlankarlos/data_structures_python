# deque in Python - Double Ended Queue
from random import randint


class Deque:
    def __init__(self):
        self.deque = []
        self.lenght_deque = 0

    def push_front(self, valor):
        self.deque.insert(0, valor)
        self.lenght_deque += 1

    def push_back(self, valor):
        self.deque.append(valor)
        self.lenght_deque += 1

    def pop_front(self):
        if not self.empty():
            valor = self.deque.pop(0)
            self.lenght_deque -= 1
            return valor

    def pop_back(self):
        if not self.empty():
            valor = self.deque.pop(self.lenght_deque - 1)
            self.lenght_deque -= 1
            return valor

    def front(self):
        if not self.empty():
            return self.deque[0]

    def back(self):
        if not self.empty():
            return self.deque[-1]

    def empty(self):
        if self.lenght_deque == 0:
            return True

        return False

    def length(self):
        return self.lenght_deque

    def show(self):
        for item in self.deque:
            print(item, end=" ")


new_deque = Deque()
for i in range(10):
    new_deque.push_front(i + 1)
    new_deque.push_back(i + 11)

print("front: ", new_deque.front())
print("back: ", new_deque.back())
new_deque.show()
print()

for item in range(new_deque.length() // 2):
    print(f"{new_deque.pop_back()} - {new_deque.length()+1}")
    print(f"{new_deque.pop_front()} -  {new_deque.length()+1}")
