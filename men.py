frase = input("Digite uma frase: ")
vogais = "AEIOUaeiou"
contador_de_vogais = 0

for letra in frase:
    for vogal in vogais:
        if letra == vogal:
            contador_de_vogais += 1

print(contador_de_vogais)
