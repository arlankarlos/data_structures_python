# graph algorithm in Python
from collections import defaultdict


# vertex
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


# arc
class Friendship:
    def __init__(self, person1, person2):
        self.person1 = person1
        self.person2 = person2

    def get_person1(self):
        return self.person1

    def get_person2(self):
        return self.person2


# graph
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_arcs(self, person1, person2):
        self.graph[person1.get_name()].append(person2)
        self.graph[person2.get_name()].append(person1)

    def show_friends(self, person):
        for friend in self.graph[person.get_name()]:
            print(f"{friend.get_name()}")


graph = Graph()
p1 = Person("Alice", 25)
p2 = Person("Bob", 30)
p3 = Person("Charlie", 35)
p4 = Person("David", 40)
p5 = Person("Eve", 45)

graph.add_arcs(p1, p2)
graph.add_arcs(p1, p3)
graph.add_arcs(p2, p4)
graph.add_arcs(p4, p3)
graph.add_arcs(p3, p5)
graph.add_arcs(p5, p1)


print("\np1:")
graph.show_friends(p1)
print("\np3:")
graph.show_friends(p3)
print("\np4:")
graph.show_friends(p4)
