# Ceaser Cypher algorithm in Python


def encriptar(texto, chave):

    lista = list(texto)
    texto_criptografado = ""

    for i in lista:
        ordem_caracter = (ord(i) - ord("A") + chave) % 26
        texto_criptografado += chr(ordem_caracter + ord("A"))
    return texto_criptografado


def descriptografar(texto, chave):

    lista = list(texto)
    texto_descriptografado = ""

    for i in lista:
        ordem_caracter = (ord(i) - ord("A") - chave) % 26
        texto_descriptografado += chr(ordem_caracter + ord("A"))
    return texto_descriptografado

print(encriptar("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 23))
print(descriptografar("XYZABCDEFGHIJKLMNOPQRSTUVW", 23))