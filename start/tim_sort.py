# tim sort in Python
import operator


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_nome(self):
        return self.nome

    def get_idade(self):
        return self.idade

    # def __str__(self):
    #     return f"{self.nome} - {self.idade}"

    def __repr__(self):
        return f"{self.nome} - {self.idade}"

    def __lt__(self, other):
        return self.idade < other.idade

    def __eq__(self, other):
        return self.idade == other.idade

    def __gt__(self, other):
        return self.idade > other.idade


p1 = Pessoa("João", 20)
p2 = Pessoa("Maria", 30)
p3 = Pessoa("José", 25)
p4 = Pessoa("Ana", 25)
p5 = Pessoa("Carlos", 40)
p6 = Pessoa("Marta", 35)
p7 = Pessoa("Pedro", 45)
p8 = Pessoa("Paula", 50)
p9 = Pessoa("Felipe", 55)
p10 = Pessoa("Fernanda", 60)

pessoas = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
pessoas.sort(key=operator.attrgetter("idade"))
for pessoa in pessoas:
    print(pessoa)

pessoas.sort(key=operator.attrgetter("idade"), reverse=True)
for pessoa in pessoas:
    print(pessoa)
