# binary search in Python


def busca_binaria(lista, chave, inicio, fim):

    if inicio > fim:
        return False

    meio = (inicio + fim) // 2

    if chave == lista[meio]:
        return True

    if chave < lista[meio]:
        return busca_binaria(lista, chave, inicio, meio - 1)
    return busca_binaria(lista, chave, meio + 1, fim)

lista = [11, 5, 10, 20, 15, 4]
chave = 30
lista.sort()

if busca_binaria(lista, chave, 0, len(lista) - 1) is True:
    print('Elemento encontrado')
else:
    print('Elemento não encontrado')