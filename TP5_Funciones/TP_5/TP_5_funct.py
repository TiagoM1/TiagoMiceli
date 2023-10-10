import math
from math import sqrt


#Ejercicio 1

def chk_dni(dni):
    #Convertir a string el dni que se pasa como int
    dni_string = str(dni)
    #guardamos el len en una variable
    dni_len = len(dni_string)
    #Hacemos la verificacion, si tiene 7 u 8 digitos, entonces retorna true, en caso contrario falso
    if dni_len == 7 or dni_len == 8:
        print("Dni introducido correctamente")
        return True
    else:
        print("El dni introducido es incorrecto")
        return False
print("Ejercicio 1 FIN")
print(" ")

#Ejercicio 2

def lng_word(chain):
    # Eliminar espacios en blanco al principio y al final de la cadena
    chain = chain.strip()
    
    # Dividir la cadena en palabras usando espacios como delimitador
    words = chain.split()

    if words:              # Verificar si hay palabras en la cadena
        last_word = words[-1]    # Obtener la última palabra
        leng = len(last_word)    # Calcular la longitud de la última palabra
        return leng
    else:          # Si no hay palabras, la longitud es 0
        return 0

#Ejercicio 3

# Función para validar el DNI
def check_dni(dni):
    return len(dni) in (7, 8) and dni.isdigit()

# Función para generar el identificador
def generate_identificator(name, surname, dni):
    first_name = name.split()[0]
    surname_length = len(surname)
    dni_prefix = dni[:3]
    return f"{first_name}{surname_length}{dni_prefix}"


#Ejercicio 4

def is_multiple(num1, num2):            #Función para verificar si el primer número es múltiplo del segundo
    if num2 == 0:
        return False                    #Evitar división por cero
    return num1 % num2 == 0

#Ejercicio 5

def average_temperature(min,max):
    return str((min + max) / 2)

#Ejercicio 6

def spacer(text):
    if not text.isalpha():
        return "Ingrese solo letras, por favor."
    
    spaced_text = ""
    for char in text:
        spaced_text += char + " "
    
    return spaced_text.strip()

#Ejercicio 7

#Funcion que imprime el mayor y menor numero ingresado
def min_max():
    num = ""
    print("Ingrese numeros enteros, escriba 0 para salir")
    while num != "0":
        num = str(input("> "))                                   #Bucle para inicializar las variables minimum, maxi
        if num.isdigit() or (num[0]=="-" and num[1:].isdigit()): #Compruebo que el valor ingresado sea un número se entero
            num = int(num) 
            maxi = num                                              #Inicializo el mínimo y el maximo con esta valor
            minimum = num
            break
        else:
            print("El valor ingresado no es un número entero  \nIngrese un números enteros, escriba 0 para salir") #Si no llega a ser un número entero se repite el bucle haste que elija un valor válido

    while num != 0:                                                 #Este otro bucle será el que pida todos los números que quiera ingresar y guardará el valor máximo y mínimo
        num = str(input("> "))
        if num.isdigit() or (num[0]=="-" and num[1:].isdigit()):
            num = int(num)
            minimum = num if num<minimum else minimum
            maxi = num if num>maxi else maxi
        else:
            print("El valor ingresado no es un número entero  \nIngrese números enteros, escriba 0 para salir")

    print(f"El Mayor número ingresado es {maxi}")                    #Imprime el numero máximo y mínimo ingresado
    print(f"El Menor número ingresado es {minimum}")

print("Se le va a pedir que ingrese numeros enteros y el programa devolverá el mayor y el menor numero ingresado")

#Ejercicio 8

print("Ejercicio 8")
def calc_area_perimetro(radio):
    #Un pequeño manejo de tipo de datos
    if type(radio) == int:
        #Calculamos y usamos math.pi para el numero pi
        per = 2 * math.pi * radio
        area = math.pi * radio**2
        per = "{:.2f}".format(per)
        area = "{:.2f}".format(area)
        print(f"El area del circulo con circunferencia: {radio}, es de: {area} \n El perimetro del circulo con circunferencia: {radio}, es de: {per}")
        return area, per
    else:
        #Transformamos en int
        radio_int = int(radio)
        #Calculamos
        per = 2 * math.pi * radio_int
        area = math.pi * radio_int**2
        per = "{:.2f}".format(per)
        area = "{:.2f}".format(area)
        print(f"El area del circulo con circunferencia: {radio}, es de: {area} \n El perimetro del circulo con circunferencia: {radio}, es de: {per}")
        return area, per
print("Ejercicio 8 FIN")
print(" ")

#Ejercicio 9

def login(user, psswrd, tries):  # Definir la subrutina login
    corr_user = "usuario1"
    corr_psswrd = "asdasd"

    if user == corr_user and psswrd == corr_psswrd:
        return True, tries  # Login exitoso, devuelve Verdadero y el número de intentos
    else:
        tries += 1  # Incrementar el número de intentos
        return False, tries  # Login fallido, devuelve Falso y el número de intentos

#Ejercicio 10

#Funcion en la que se aplican los descuentos
def apply_discounts(cart, discounts):
    final_price = 0
    
    for product, price in cart.items():
        if product in discounts:
            discount = discounts[product]
            discounted_price = price * (1 - discount / 100)
            final_price += discounted_price
        else:
            final_price += price
    
    return final_price
# Función para ingresar el carrito y los descuentos por parte del usuario
def cart_and_discounts():
    cart = {}
    discounts = {}
    
    while True:
        product = input("Ingrese el nombre del producto (o presione Enter para finalizar): ")
        if not product:
            break
        price = float(input(f"Ingrese el precio de '{product}': "))
        cart[product] = price
        discount = float(input(f"Ingrese el porcentaje de descuento para '{product}': "))
        discounts[product] = discount
    
    return cart, discounts

#Ejercicio 11

def apply_function(function, list):         #Definir una funcion que toma ambos argumentos
    result =[]                              #Crear una lista vacía para almacenar los resultados
    for element in list:
        result.append(function(element))    #Aplicar la función dada al elemento actual y agregar el resultado a la lista
    return result                           #Devolver la lista resultado que contiene los resultados de aplicar la función a cada elemento

def square(x):              #Definir una función para calcular el cuadrado de un número
    return x**2

#Ejercicio 12

def frase_counter(frase, dictionary, aux):
    for i in range(len(frase)):
        if frase[i] != " ":
            aux += frase[i]
        else:
            dictionary[aux] = len(aux)
            aux = ""

    if aux:
        dictionary[aux] = len(aux)
    return dictionary

#Ejercicio 13

def vector_modulus_calculator (cathetus_1, cathetus_2):
    return sqrt((cathetus_1 ** 2) + (cathetus_2 ** 2))

#Ejercicio 14

def prime_num(num):                  
    if num <= 1:            #Devuelve falso si el número es 0 o 1
        return False
    elif num <= 3:          #Devuelve true si el número es 3 o 2
        return True
    elif num % 2 == 0 or num % 3 == 0:  #Si es divisible por 2 y 3 es falso
        return False
    i = 5
    while i * i <= num:      
        if num % i == 0 or num % (i + 2) == 0:   #Si llega a ser divisible por alguna de estas opciones sera falso, sino repetira el procedimiento incrementandi i en 6
            return False
        i += 6
    return True

#Ejercicio 15

def factorial_num(num, salir):
    read_number = 0
    while True:
        print(" ")
        aux = num
        if num == 0:
            num = 1
            print(f"El factorial del numero: {aux}, es de: 1")
            read_number += 1
            print(" ")
        else:
            for i in range(num):
                if i == 0:
                    continue
                num = num * i
            print(f"El factorial del numero: {aux}, es de: {num}")
            read_number += 1
            print(" ")
        if salir == "si":
            break
        elif salir == "no":
            continue
    print("La cantidad de numeros pedidos es de: ", read_number)
    return num

print("Ejercicio 15 FIN")
print(" ")

#Ejercicio 16

def freq(a, b): #Funcion para calcular frecuencia
    ocurrency = 0
    num_string = str(a)
    
    for d in num_string:
        if d == b:
            ocurrency += 1
    
    return ocurrency

# Función para validar si es un número entero
def whol_num(stng):
    return stng.isdigit() or (stng[0] == '-' and stng[1:].isdigit())

# Función para validar si es un solo dígito
def dig_func(stng):
    return len(stng) == 1 and stng.isdigit()

#Ejercicio 17

# Función para verificar si un número es primo
def es_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

# Función para calcular la suma de los dígitos de un número
def suma_digitos(numero):
    suma = 0
    while numero > 0:
        suma += numero % 10
        numero //= 10
    return suma

# Función para contar la frecuencia de un dígito en un número
def contar_digitos(numero, digito):
    count = 0
    while numero > 0:
        if numero % 10 == digito:
            count += 1
        numero //= 10
    return count 

# Función para calcular el factorial de un número
def factorial(numero):
    if numero == 0:
        return 1
    return numero * factorial(numero - 1)
