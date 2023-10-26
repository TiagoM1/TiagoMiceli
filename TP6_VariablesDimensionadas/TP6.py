#--------------------Ejercicio 1--------------------

#Defino las variables que necesite durante todo el programa
record = []
validator = False
number= input("Ingrese un número: ")

#Bucle para evitar tener que reiniciar el programa cada vez que se ingrese un dato inválido
while (validator == False):
    #Si lo ingresado por el usuario no es un número, se le comunica y se reinicia el bucle entero
    if (number.isdigit() == False ):
        print("Ingrese SÓLO números, por favor.")
        number= input("ingrese otro número: ")
        continue
    #Si el usuario ingresa la condicion de salida (es decir, 0), se rompe el bucle
    if (number == "0"):
        print("Los números ingresados fueron: " + ", ".join(record))
        validator= True
        continue
    #Si lo ingresdo por el usuario es un número y no es un 0, se añade al array dicho número y se pide otro número
    record.append(number)
    number= input("Ingrese otro número: ")


#--------------------Ejercicio 2--------------------

#Se me pide solicitar al usuario que ingrese un número y, si el número está en la lista, eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar
def check_integer():
    while True:
        num = input("> ")
        if num.isdigit():
            break
        else: 
            print("No ha ingresado un valor numérico entero, ingrese un número entero")
    return int(num)

print("Ingrese un número entero")
num = check_integer()
list_num = [13,21,4,8,81,32,1,21]

if num in list_num:
    print("Eliminando primera ocurrencia")
    list_num.remove(num)                    
else: 
    print("El número ingresado no se encuentra incluido en la lista, no es posible eliminarlo")
print(list_num)

#--------------------Ejercicio 3--------------------

numbers = [1,2,3,4,5,6,7,8,9]
print(f"Sumatoria de la lista: {sum(numbers)}")

#--------------------Ejercicio 4--------------------

def filter_numbers(input_list, limit):                                  #Funcion que crea la nueva lista de numeros
    new_list = [number for number in input_list if number < limit]
    return new_list

original_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]                    #Para este ejercicio se usa la lista generada en el primer punto

limit_number = int(input("Por favor, introduce un número: "))           #Solicitar al usuario un número

filtered_list = filter_numbers(original_list,limit_number)              #Llamar a la funcion y obtener una nueva lista

print("Elementos menores que", limit_number, ":")                       #Imprimir la nueva lista e iterar por ella
for element in filtered_list:
    print(element)

#--------------------Ejercicio 5--------------------

import random

#Generador de listas, con numeros aleatorios del 0 al 100 y de un tamaño aleatorio mayor a 7 pero menor a 20 la lista
def generator_list():
    aux_list = []
    num_verify = 1
    aux_around = 0
    while num_verify < 100:
        num = random.randint(0, 100)
        aux_list.append(num)
        aux_around += 1
        num_verify += random.randint(0, 25)
        if len(aux_list) >= 10:
            return aux_list
    if aux_around <= 7:
        return generator_list()
    else:
        return aux_list

#Basicamente se agrega como argumento predeterminado una lista vacia, en caso de que no se pase una
def lista_tupla_numbers(list=[]):
    #si la lista esta vacia, genero una lista con la funcion generator_list()
    if len(list) == 0:
        lista_numbers = generator_list()
        #Auxiliar para la nueva lista
        lista_tupla_num = []
        #Recorro la lista
        for number in lista_numbers:
            #Guardo cuantas veces aparece el numero en la lista
            count_number = lista_numbers.count(number)
            #Verifico que no se haya agregado a la nueva lista
            if (number, count_number) not in lista_tupla_num:
                lista_tupla_num.append((number, count_number))
        #Retorno la nueva lista
        return lista_tupla_num
    #Exactamente lo mismo que arriba, solo que con la lista pasada por el argumento
    else:
        lista_tupla_num = []
        for number in list:
            count_number = list.count(number)
            if (number, count_number) not in lista_tupla_num:
                lista_tupla_num.append((number, count_number))
        return lista_tupla_num

#--------------------Ejercicio 6--------------------

# listas para almacenar los nombres de los alumnos de nivel primario y secundario
first_name = []
scnd_name = []

# Solicitar nombres de alumnos de nivel primario
print("Ingrese los nombres de los alumnos de nivel primario (ingrese 'x' para finalizar):")
while True:
    name = input()
    if name == 'x':
        break
    first_name.append(name)

# Solicitar nombres de alumnos de nivel secundario
print("Ingrese los nombres de los alumnos de nivel secundario (ingrese 'x' para finalizar):")
while True:
    name = input()
    if name == 'x':
        break
    scnd_name.append(name)

# nombres de todos los alumnos de nivel primario y secundario sin repeticiones
all_name = list(set(first_name + scnd_name))
print("\nNombres de todos los alumnos sin repeticiones:")
for name in all_name:
    print(name)

#nombres que se repiten entre los alumnos de nivel primario y secundario
rep_name = list(set(first_name) & set(scnd_name))
print("\nNombres que se repiten entre primario y secundario:")
for name in rep_name:
    print(name)

#nombres de nivel primario no se repiten en los de nivel secundario
uniq_frst_name = list(set(first_name) - set(scnd_name))
print("\nNombres de nivel primario que no se repiten en nivel secundario:")
for name in uniq_frst_name:
    print(name)

#--------------------Ejercicio 7--------------------

#Inicializo un diccionario para almacenar las ocurrencias de cada carácter
occurrences = {}

#Inicializo un contador para rastrear la cantidad de strings procesados
string_counter = 0

#Proceso strings hasta que se hayan procesado 50 o más
while string_counter < 50:
    string_entered = input("Ingresa un string (o presiona Enter para finalizar): ")
    
    #Verifico si el usuario presionó Enter para finalizar
    if not string_entered:
        break
    
    #Incremento el contador de strings procesados
    string_counter += 1
    
    #Recorro cada carácter en el string y actualizo las ocurrencias en el diccionario
    for i in string_entered:
        if i in occurrences:
            occurrences[i] += 1
        else:
            occurrences[i] = 1

#Imprimo las ocurrencias de cada carácter
for i, amount in occurrences.items():
    print(f"'{i}': {amount}")


##--------------------Ejercicio 8--------------------

import random

#Defino todas las variables que voy a necesitar a lo largo de todo el programa
goals= []
rows= 10
columns= 10
amount_w= [0] * rows
amount_t= [0] * rows
amount_d= [0] * rows
received= 0
made= 0
points= 0

#Relleno toda la tabla (array) de los goles de cada equipo
for i in range(rows):
    row = []
    for i in range(columns):
        random_number = random.randint(1, 10)
        row.append(random_number)
    goals.append(row)

for i in range(len(goals)):
    goals[i][i] = 0

#Consigna 1º: "Lea el cuadro de goles en un arreglo de dos dimensiones"
print("----------<<<<<Tabla de Goles de Todos los Equipos>>>>>----------")
print("")
for row in goals:
    print(row)

print("")
print("----------<<<<<Rendimiento de Cada Equipo>>>>>----------")
print("")

#Consigna 2º: "Muestre para cada equipo la cantidad de triunfos, empates y derrotas"
for i in range(rows):
    for j in range(columns):
        if goals[i][j] > goals[j][i]:
            amount_w[i] += 1
        elif goals[i][j] == goals[j][i]:
            amount_t[i] += 1
        else:
            amount_d[i] += 1

for i in range(rows):
    print(f"Equipo {i + 1}: Triunfos - {amount_w[i]}, Empates - {amount_t[i]}, Derrotas - {amount_d[i]}")

print("")
print("----------<<<<<Diferencia de Goles Totales>>>>>----------")
print("")

#Consigna 3º: "Muestre la diferencia entre el total de goles marcados y el total de goles recibidos"
for i in range(rows):
    for j in range(columns):
        received+= goals[i][j]
        made+= goals[j][i]
    print(f"Equipo {i + 1}: Recibidos - {received}; Marcados - {made}")
    received=0
    made= 0

print("")
print("----------<<<<<Puntos de los Equipos>>>>>----------")
print("")

#Consigna 4º: "Determine la cantidad de puntos obtenidos por cada equipo"

'''(Aclaración)
Los puntos se proporcionan teniendo en cuenta el siguiente criterio:
Victorias: +3pts; Empates: +1pto; Derrotas: +0pts'''

for i in range(rows):
    points= (3 * amount_w[i] + amount_t[i])
    print(f"Equipo {i + 1}: {points}pts")


#--------------------Ejercicio 9--------------------

# Escribir un programa que simule el juego clásico de Memoria (Memotest) utilizando matrices.
# Funcion que pide ingresar un numero entero y en el rango permitido de las filas
def check_row():
    while True:
        print("fila:")
        row = str(input("> "))
        if row.isdigit:
            row = int(row)-1
            if row>=0 and row<4:
                break
            else:
                print("El número debe ser del 1 al 4, vuelva a ingresar un número")
        else:
            print("El valor ingresado debe ser un número entero")
    return row

#Funcion que pide ingresar un numero entero y en el rango permitido de las columnas
def check_col():
    while True:
        print("columna:")
        col = str(input("> "))
        if col.isdigit:
            col = int(col)-1
            if col>=0 and col<6:
                break
            else:
                print("El número debe ser del 1 al 6, vuelva a ingresar un número")
        else:
            print("El valor ingresado debe ser un número entero")
    return col

#Código Principal
#Inicializando matriz con los valores y otra igual vacía
cards = [[1,4,7,11,3,9],[12,10,5,8,6,2],[7,12,6,9,1,3],[10,5,8,4,2,11]] 
cards_2 = [[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "]]

print("Vamos a jugar al memotest")

#Mostrar las posiciones de los números vacias
print("Posiciones")
for i in range(len(cards)):
    for j in range(len(cards[0])):
        print(f"[{cards_2[i][j]}] ", end="")
    print("")

while True:
    count = 0
    print("\nIngrese la posicion del primer número  \n")
    row = check_row()
    col = check_col()

    #Verifico que no vuelva a eligir un número ya adivinado
    if cards_2[row][col] == str(cards[row][col]):
        print(f"ya has encontrado el número {cards[row][col]}, elija de nuevo fila y columna")
        continue
    
    #Ingreso a la matriz vacia el número escogido
    cards_2[row][col] = str(cards[row][col])
    
    #muestro el número escogido
    for i in range(len(cards)):
        for j in range(len(cards[0])):
            print(f"[{cards_2[i][j]}] ", end="")
        print("")
    
    print("Ingrese la posicion del segundo número")
    row_2 = check_row()
    col_2 = check_col()

    #Verifico que no vualva a eligir un número ya adivinado
    if cards_2[row_2][col_2] == str(cards[row_2][col_2]):
        print(f"ya has elegifo el número {cards[row_2][col_2]}, elija de nuevo fila y columna")
        cards_2[row][col] = " "
        continue
    
    #Ingreso a la matriz vacia el numero escogido
    cards_2[row_2][col_2] = str(cards[row_2][col_2])
    
    #muestro el número escogido
    for i in range(len(cards)):
        for j in range(len(cards[0])):
            print(f"[{cards_2[i][j]}] ", end="")
        print("")

    #Informo si hay coincidencia, en caso de que si, los valores se guardan y verifico si ya se encontraron todos los números  
    if cards_2[row][col] == cards_2[row_2][col_2]:
        print("\nAdivinaste! Continúa asi")
        for element in cards_2:
            if (" " in element):
                count += 1
        if count == 0:
            print("Felicidades, conseguiste adivinar todos los pares de números")
            break

    #En caso de que no, a los números escogido no se guardan en la tabla 
    else:
        print("\nNo hay coincidencia vuelve a intentar")
        cards_2[row][col] = " "
        cards_2[row_2][col_2] = " "

#--------------------Ejercicio 10--------------------

def main_diagonal(matrix):
    return [matrix[i][i] for i in range(len(matrix))]

def reverse_diagonal(matrix):
    n = len(matrix)
    return [matrix[i][n - 1 - i] for i in range(n)]

# Definición de la matriz
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Compruebo que es cuadrada
if len(matrix) == len(matrix[0]):
    main_diagonal = main_diagonal(matrix)
    reverse_diagonal = reverse_diagonal(matrix)
    
    print(f"Diagonal principal: {main_diagonal}")
    print(f"Diagonal inversa: {reverse_diagonal}")
else:
    print("La matriz no es cuadrada.")

#--------------------Ejercicio 11--------------------

def currency_symbol(currency):                                     #Función que crea el diccionario y verifica si la palabra ingresada se encuentra dentro del mismo
    dictionary = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}
    if currency in dictionary:
        symbol = dictionary[currency]
        return f"El símbolo de {currency} es {symbol}"
    else:
        return "La divisa ingresada no está en el diccionario"
    
currency = input("Ingrese una divisa: ").title()      #Pedir al usuario que ingrese una divisa

result = currency_symbol(currency)                  #Llamar a la función e imprimir el resultado
print (result)

#--------------------Ejercicio 12--------------------

# nombre, edad, dirección y teléfono 


def print_personal_information():
    #Pido la informacion
    #Forma 1
    #Crearlo, la diccionario, con las variables ya asignadas
    # nombre = input("Ingrese su nombre: ")
    # edad = int(input("Ingrese su edad: "))
    # dirreccion = input("Ingrese su dirreccion: ")
    # telefono = input("Ingrese su telefono: ")
    # #Lo agrego a un diccionario
    # diccionario_cosas_personales = {
    #     "nombre": nombre,
    #     "edad": edad,
    #     "direccion": dirreccion,
    #     "telefono": telefono
    # }


    #Forma 2
    #Con update
    # nombre = input("Ingrese su nombre: ")
    # edad = int(input("Ingrese su edad: "))
    # dirreccion = input("Ingrese su dirreccion: ")
    # telefono = input("Ingrese su telefono: ")
    # diccionario_cosas_personales = {}
    # diccionario_cosas_personales.update({"nombre": nombre, "edad": edad,"direccion": dirreccion,"telefono": telefono})


    #Forma 3
    #De Asignacion, asignar mientras pides la informacion
    diccionario_cosas_personales = {}
    diccionario_cosas_personales['nombre'] = input("Ingrese su nombre: ")
    diccionario_cosas_personales['edad'] = int(input("Ingrese su edad: "))
    diccionario_cosas_personales['direccion'] = input("Ingrese su dirreccion: ")
    diccionario_cosas_personales['telefono'] = input("Ingrese su telefono: ") 

    
    #Imprimo la informacion desde el diccionario
    print(f"El usuario {diccionario_cosas_personales['nombre']} tiene {diccionario_cosas_personales['edad']} años, vive en {diccionario_cosas_personales['direccion']} y su numero de telefono es {diccionario_cosas_personales['telefono']}")

#--------------------Ejercicio 13--------------------

# Diccionario con los precios de las frutas
price_f = {
    "manzana": 200.0,
    "banana": 1500.0,
    "uva": 300.0,
    "pera": 250.0,
    "naranja": 600.0
}

# Pedir al usuario que ingrese la fruta y la cantidad en kilos
fruit = input("Ingrese el nombre de la fruta: ").lower()
kg = float(input("Ingrese la cantidad en kilos: "))

# Verificar si la fruta está en el diccionario de precios
if fruit in price_f:
    total_price = price_f[fruit] * kg
    print(f"El precio de {kg} kilos de {fruit} es: ${total_price:.2f}")
else:
    print(f"Lo siento, en esta verduleria no tenemos {fruit}.")