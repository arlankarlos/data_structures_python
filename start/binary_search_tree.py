# binary search tree in Python
from random import sample


class Node:
    def __init__(self, label):
        self.label = label
        self.left = None
        self.right = None

    def get_label(self):
        return self.label

    def set_label(self, label):
        self.label = label

    def get_left(self):
        return self.left

    def set_left(self, left):
        self.left = left

    def get_right(self):
        return self.right

    def set_right(self, right):
        self.right = right


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, label):
        # cria um novo nó
        node = Node(label)

        # verifica se a árvore está vazia
        if self.empty():
            self.root = node
        else:
            # árvore não vazia, insere recursivamente
            dad_node = None
            current_node = self.root

            while True:
                if current_node is not None:
                    dad_node = current_node

                    # verifica se o novo nó é menor ou maior que o atual
                    if node.get_label() < current_node.get_label():
                        # vai para esquerda
                        current_node = current_node.get_left()
                    else:
                        current_node = current_node.get_right()
                else:
                    # se current_node is None, encontrou onde inserir
                    if node.get_label() < dad_node.get_label():
                        dad_node.set_left(node)
                    else:
                        dad_node.set_right(node)
                    break

    def remove(self, label):
        """
        3 casos

        Caso 1
        o nó a ser removido não tem filhos
        esee caso é simples, bastar definir a ligação
        do pai para o None

        Caso 2
        o nó a ser removido tem somente 1 filho
        basta colocar o seu filho no lugar dele

        Caso 3
        o nó a ser removido possui dois filhos
        basta pegar o menor elemento da subárvore a direita

        """

        dad_node = None
        current_node = self.root

        while current_node is not None:
            # verifica se encontrou o nó a ser removido
            if label == current_node.get_label():
                
                # caso 1: o nó a ser removido não possui filhos (só folha)
                if current_node.get_left() is None and current_node.get_right() is None:
                    
                    # verifica se é a raiz
                    if dad_node is None:
                        self.root = None
                    else:
                        # verifica se é filho a esquerda ou a direita
                        if dad_node.get_left() == current_node:
                            dad_node.set_left(None)
                        elif dad_node.get_right() == current_node:
                            dad_node.set_right(None)

                # caso 2: o nó a ser removido tem somente 1 filho
                elif (
                    current_node.get_left() is None
                    and current_node.get_right() is not None
                ) or (
                    current_node.get_left() is not None
                    and current_node.get_right() is None
                ):
                    # verifica se o nó a ser removido é a raiz
                    if dad_node is None:
                        # verifica se o filho current_node é filho a esquerda
                        if current_node.get_left() is not None:
                            self.root = current_node.get_left()
                        else:
                            self.root = current_node.get_right()
                    else:
                        # se não for a raiz, verifica se o nó a ser removido é filho a esquerda
                        if current_node.get_left() is not None:
                            # verifica se o current_node é filho a esquerda
                            if (
                                dad_node.get_left()
                                and dad_node.get_left().get_label()
                                == current_node.get_label()
                            ):
                                dad_node.set_left(current_node.get_left())
                            else:
                                # senão current_node é filho a direita
                                dad_node.set_right(current_node.get_left())
                        # senão o filho de current_node é filho a direita
                        else:
                            # verifica se o current_node é filho a esquerda
                            if (
                                dad_node.get_left()
                                and dad_node.get_left().get_label()
                                == current_node.get_label()
                            ):
                                dad_node.set_left(current_node.get_right())
                            else:
                                dad_node.set_right(current_node.get_right())

                # caso 3: o nó a ser removido possui dois filhos
                # pega-se o menor elemento da subárvore a direita
                elif (
                    current_node.get_left() is not None
                    and current_node.get_right() is not None
                ):
                    dad_smaller_node = current_node
                    smaller_node = current_node.get_right()
                    next_smaller = current_node.get_right().get_left()

                    while next_smaller is not None:
                        dad_smaller_node = smaller_node
                        smaller_node = next_smaller
                        next_smaller = next_smaller.get_left()

                    # verifica se o nó a sesr removido á raiz
                    if dad_node is None:
                        # caso especial: o nó que vai ser a nova raiz é filho da raiz
                        # self.root = smaller_node
                        if (
                            self.root.get_right().get_label()
                            == smaller_node.get_label()
                        ):
                            smaller_node.set_left(self.root.get_left())
                        else:
                            """
                                verifica se o smaller node é filho a esquer ou
                                a direita para definir None o smaller_node
                            """
                            if (
                                dad_smaller_node.get_left()
                                and dad_smaller_node.get_left().get_label()
                                == smaller_node.get_label()
                            ):
                                dad_smaller_node.set_left(None)
                            else:
                                dad_smaller_node.set_right(None)

                            # define os filhos a direita e a esquerda de smaller_node
                            smaller_node.set_left(current_node.get_left())
                            smaller_node.set_right(current_node.get_right())
                        # faz com que o smaller_node seja a raiz
                        self.root = smaller_node
                    else:
                        """
                            verifica se current_node é filho a esquerda ou a direita
                            para definir o smaller_node como filho do pai do current_node
                            (dad_node)
                        """
                        if (
                            dad_node.get_left()
                            and dad_node.get_left().get_label() == current_node.get_label()
                        ):
                            dad_node.set_left(smaller_node)
                        else:
                            dad_node.set_right(smaller_node)

                        """
                            verifica se o smaller_node é filho a esquerda ou
                            a direita para definir None o smaller_node
                        """
                        if (
                            dad_smaller_node.get_left()
                            and dad_smaller_node.get_left().get_label()
                            == smaller_node.get_label()
                        ):
                            dad_smaller_node.set_left(None)
                        else:
                            dad_smaller_node.set_right(None)
                            
                        # define os filhos a direita e a esquerda de smaller_node
                        smaller_node.set_left(current_node.get_left())
                        smaller_node.set_right(current_node.get_right())
                break

            # atualiza o ponteiro para o pai do current_node
            dad_node = current_node
            
            # verifica se vai para esquerda ou direita
            if label < current_node.get_label():
                # vai para esquerda
                current_node = current_node.get_left()
            else:
                # vai para direita
                current_node = current_node.get_right()
                        

    def empty(self):
        if self.root is None:
            return True
        return False

    # mostra em pré-ordem (raiz-esq-dir)
    def show(self, current_node):
        if current_node is not None:
            print(f"{current_node.get_label()} ", end=" ")
            self.show(current_node.get_left())
            self.show(current_node.get_right())

    def get_root(self):
        return self.root


# tests
new_binary_search_tree = BinarySearchTree()
cases = [8,3,1,6,4,7,10,14,13,9]
for i in cases:
    new_binary_search_tree.insert(i)
print(new_binary_search_tree.get_root().get_label())
new_binary_search_tree.show(new_binary_search_tree.get_root())
new_binary_search_tree.remove(8)
print('\n\n')
new_binary_search_tree.show(new_binary_search_tree.get_root())
# new_binary_search_tree.remove(10)
print('\n\n')
new_binary_search_tree.show(new_binary_search_tree.get_root())
# new_binary_search_tree.remove(6)
print('\n\n')
new_binary_search_tree.show(new_binary_search_tree.get_root())
