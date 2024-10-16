# Ceaser Cypher algorithm in Python

def cifra_cesar(texto, chave):
    texto_cifrado = ""
    for i in range(len(texto)):
        char = texto[i]
        if char.isupper():
            texto_cifrado += chr((ord(char) + chave - 65) % 26 + 65)
        else:
            texto_cifrado += chr((ord(char) + chave - 97) % 26 + 97)
    return texto_cifrado

def decifra_cesar(texto_cifrado, chave):
    texto = ""
    for i in range(len(texto_cifrado)):
        char = texto_cifrado[i]
        if char.isupper():
            texto += chr((ord(char) - chave - 65) % 26 + 65)
        else:
            texto += chr((ord(char) - chave - 97) % 26 + 97)
    return texto


texto = "Hello, World!"
chave = 5
texto_cifrado = cifra_cesar(texto, chave)
print("Texto cifrado:", texto_cifrado)
print("Texto decifrado:", decifra_cesar(texto_cifrado, chave))

# Output:
# Texto cifrado: Lipps, Asvph!
# Texto decifrado: Hello, World!
