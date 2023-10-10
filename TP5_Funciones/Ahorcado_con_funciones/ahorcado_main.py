
import random
import ahorcado_funciones


word_list = ["carpa", "mochila", "chocolate", "pancho", "panqueque", "deporte", "messi"]
random_word = random.choice(word_list)
fill_word = ["_ "] * len(random_word)
exit = False
life = 6
while(life > 0 and exit == False):
    if "_ " in fill_word:
        print(f"Intentos: {str(life)}, Palabra: {''.join(fill_word)}")
        
        letter = input("Letra a buscar: ")

# filtro por si se ingresa la palabra completa o una letra

        if (letter.isalpha() and len(letter) == 1  or letter == random_word):

            if letter == random_word:
                fill_word = letter
                exit = True
            elif letter in random_word:
# la funcion busca la letra en la palabra de la lista y si existe, reeplaza el _ 

                fill_word, random_word, letter = ahorcado_funciones.complete_word(fill_word,random_word, letter)
            else:
# la funcion verifica si la palabra no contiene la letra, se resta un intento

                life, exit = ahorcado_funciones.wrong_letter(life, exit)
        else:
            print("--- Ingresar una letra ---")
    else:
        exit = True
if life > 0:
    print(f"--- Palabra Encontrada! {''.join(fill_word)} ---")
else:
    print(f"--- Sin Intentos, Palabra: {random_word} ---")










