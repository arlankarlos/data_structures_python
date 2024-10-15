# priority queue in Python
# lista de prioridade ordenada em Python


class Person:
    """
        nome -> nome da pessoa
        prioridade -> prioridade da pessoa
    """
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
        
    def get_name(self):
        return self.name
    
    def get_priority(self):
        return self.priority
    
    
class PriorityQueue:
    
    def __init__(self):
        self.priority_queue = []
        self.lenght_priority_queue = 0
    
    # insere decrescentemente pela prioridade    
    def push(self, person):
        if self.empty():
            self.priority_queue.append(person)
        else:
            flag_push = False
            
            # procura-se onde inserir para manter a fila ordenada
            for i in range(self.lenght_priority_queue):
                if self.priority_queue[i].get_priority() < person.get_priority():
                    self.priority_queue.insert(i, person)
                    flag_push = True
                    break
            if not flag_push:
                # se entrou aqui é porque tem que inserir ao finall
                self.priority_queue.insert(self.lenght_priority_queue, person)
        self.lenght_priority_queue += 1
    
    
    def pop(self):
        if not self.empty():
            self.lenght_priority_queue -= 1
            return self.priority_queue.pop(0)
    
    
    def empty(self):
        if self.lenght_priority_queue == 0:
            return True
        return False
    
    def length(self):
        return self.lenght_priority_queue
    
    def show(self):
        for person in self.priority_queue:
            print(f'Nome:\t\t {person.get_name()}')
            print(f'Prioridade:\t {person.get_priority()}')
            print()
            

# criar os objetos
person1 = Person('Joaquim', 28)
person2 = Person('Maria', 1)
person3 = Person('Jose', 4)
person4 = Person('Joao', 2)

# criar a fila de prioridades e inserir os elementos
priority_queue = PriorityQueue()
priority_queue.push(person1)
priority_queue.push(person2)
priority_queue.push(person3)
priority_queue.push(person4)

print('Exibir as inserções:')
priority_queue.show()
priority_queue.pop()
priority_queue.pop()
print('\nExibir as inserções:')
priority_queue.show()
priority_queue.push(Person('Goku', 30))
print('\nExibir as inserções:')
priority_queue.show()