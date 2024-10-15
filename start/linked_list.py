# linked list in Python
from random import randint


class Node:
    def __init__(self, label):
        self.label = label
        self.next = None

    def get_label(self):
        return self.label

    def set_label(self, label):
        self.label = label

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.length_list = 0


    def __str__(self):
        return str(self.head)


    def push(self, label, index):
        if index > 0:
            # cria o novo nó
            node = Node(label)

            # verifica se a lista está vazia
            if self.empty():
                self.first = node
                self.last = node
            else:
                if index == 0:
                    # inserção no início
                    node.set_next(self.first)
                    self.first = node
                elif index >= self.length_list:
                    # inserção no final
                    self.last.set_next(node)
                    self.last = node
                else:
                    # inserção no meio
                    aux_node = self.first
                    current_node = self.first.get_next()
                    current_index = 1

                    while current_node is not None:
                        if current_index == index:
                            # insere o current_node como o próximo nó
                            node.set_next(current_node)
                            # defini o node como o próximo do aux_node
                            aux_node.set_next(node)
                            break

                        aux_node = current_node
                        current_node = current_node.get_next()
                        current_index += 1
            # atualiza o tamanho da lista
            self.length_list += 1


    def pop(self, index):
        if not self.empty() and index >= 0 and index < self.length_list:
            flag_remove = False

            if self.first.get_next() is None:
                # possui apenas 1 elemento
                self.first = None
                self.last = None
                flag_remove = True
            elif index == 0:
                # remove do início, mas possui mais de 1 elemento
                self.first = self.first.get_next()
                flag_remove = True
            else:
                # se chegou aqui é porque a lista possui mais
                # de 1 elemento e a remoção não é no início
                aux_node = self.first
                current_node = self.first.get_next()
                current_index = 1

                while current_node is not None:
                    if index == current_index:
                        # o proximo nó anterior aponta para o próximo nó da corrente
                        aux_node.set_next(current_node.get_next())
                        current_node.set_next(None)
                        flag_remove = True
                        break
                    aux_node = current_node
                    current_node = current_node.get_next()
                    current_index += 1

            if flag_remove:
                # atualiza o tamanho da lista
                self.length_list -= 1


    def empty(self):
        if self.first is None:
            return True
        return False


    def length(self):
        return self.length_list


    def show(self):
        current_node = self.first
        while current_node is not None:
            print(current_node.get_label(), end=' ')
            current_node = current_node.get_next()
            
        print('')
        
        
new_linked_list = LinkedList()
print('Esta vazia?', new_linked_list.empty())
print(new_linked_list.length())
for i in range(10):
    new_linked_list.push((i+1), i+1)
    
new_linked_list.show()
print(new_linked_list.pop(0))
print(new_linked_list.pop(5))
print(new_linked_list.pop(1))
new_linked_list.show()
print(new_linked_list.length())
print('Esta vazia?', new_linked_list.empty())