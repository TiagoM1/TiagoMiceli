def complete_word(fill_word,random_word, letter):
    for i in range(len(random_word)):
        if letter == random_word[i]:
            fill_word[i] = letter
    return fill_word, random_word, letter



def wrong_letter(life, exit):
    life -= 1
    if life > 0:
        print("Intenta denuevo, Intentos: " + str(life))
    else:
        exit = True
    return life, exit