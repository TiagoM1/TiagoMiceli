# Ejercicio 1 Cifrado de Cesar

abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

corrimiento = int(input("corrimiento: "))

for i in range(5):
    cesar1 = ""
    word = (input("word: ")).upper()
    for letra in word:
        if letra != " ":
            if letra in abc:
                indice_letra = abc.index(letra)
                indice_cesar = (indice_letra + corrimiento) % 26
                letra_cesar = abc[indice_cesar]
                cesar1 += letra_cesar
            else:
                cesar1 += letra
        else:
            cesar1 += " "
    print(f"word: {word} => {cesar1}")


# Ejercicio 2 numeros pares e impares

total_pares = 0
total_impares = 0

numero = int(input("Ingrese un número (ingrese 0 para finalizar): "))

while numero != 0:
    num_str = str(numero)
    pares = 0
    impares = 0
    for digito in num_str:
        if int(digito) % 2 == 0:
            pares += 1
        else:
            impares += 1
    
    print(f"El número {numero} tiene {pares} dígitos pares y {impares} dígitos impares.")
    
    total_pares += pares
    total_impares += impares
    
    numero = int(input("Ingrese un número (ingrese 0 para finalizar): "))

print(f"Total de dígitos pares leídos: {total_pares}")
print(f"Total de dígitos impares leídos: {total_impares}")

