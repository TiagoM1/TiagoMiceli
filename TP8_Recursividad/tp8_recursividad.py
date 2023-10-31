#--------------------Ejercicio 1--------------------

#Defino la funcion recursiva
def cont_digit(num):
    num = str(num)
    #Caso base 
    if len(num) == 1:
        return int(num)
    #Si no se cumple, devuelve el primer numero, sumado a la funcion recursiva pasndole un parámetro en el cual toma un numero menos
    return int(num[0]) + cont_digit(int(num[1:]))

#Codigo principal
num = int(input("Ingrese un numero positivo entero para sumar cada uno de sus dígitos: "))
print(f"La suma edel valor de los dígitos del numero {num} es: {cont_digit(num)}")

#--------------------Ejercicio 2--------------------

def n_pow(a, b):
    if a == 1:
        return True
    elif a % b == 0 and a != 0:
        return n_pow(a // b, b)
    else:
        return False

num_1 = int(input("Ingrese un numero: "))
num_2 = int(input("Ingrese otro numero: "))

print(n_pow(num_1, num_2))

#--------------------Ejercicio 3--------------------

def find_positions(string, substring, start = 0, result = None):
    if result is None:
        result = []
    
    position = string.find(substring, start)

    if position == -1:
        return result

    result.append(position)

    return find_positions(string, substring, position + 1, result)

string_input = input("Ingrese el texto principal: ")
substring_input = input("Ingrese el texto a buscar: ")

positions = find_positions(string_input, substring_input)
print(f"Las posiciones de '{substring_input}' en '{string_input}' son: {positions}")

#--------------------Ejercicio 4--------------------

def is_even(n):         #Funcion para definir si es par
    if n == 0:
        return True  
    else:
        return is_odd(n - 1)

def is_odd(n):          #Funcion para definir si es impar
    if n == 0:
        return False  
    else:
        return is_even(n - 1)

#Función principal para obtener la entrada del usuario y verificar la paridad
while True:
    number = int(input("Ingrese un número natural: "))
    if number < 0:
        print("Por favor, ingrese un número mayor o igual a 0.")
        continue
    else:
        even = is_even(number)
        if even:
            print(f"{number} es un número par.")
        else:
            print(f"{number} es un número impar.")
    break

#--------------------Ejercicio 5--------------------

def larger_list (list):
    if len(list) == 1:
        return list[0]
    else:
        max_rest = larger_list(list[1:])
        if list[0] > max_rest:
            return list[0]
        else:
            return max_rest


My_list = [24, 28, 65, 123, 35, 928]
large_num = larger_list(My_list)
print("El mayor elemento de la lista es: ", large_num)

#--------------------Ejercicio 6--------------------

def replicate(list, num):
    # Caso base
    if not list or num == 0:
        return []

    #Cuerpo principal de la funcion recursiva
    return [list[0]] * num + replicate(list[1:], num)

#Ejemplo del funcionamiento de la función anteriormente definida, usando el ejemplo proporcionado en la consigna
original_list= [1, 3, 3, 7]
num= 2
result = replicate(original_list, num)
print(result)

#--------------------Ejercicio 7--------------------

def algo_recu_EJ7(n, p): 
    if n == 1:
        print(p)
        return p
    if n != 1:
        print(n*p)
        K = n * p + algo_recu_EJ7(n-1, p) 
        return K

n = int(input("Escriba un numero entero: "))
p = int(input("Escriba un numero entero: "))

print(algo_recu_EJ7(n, p))


#--------------------Ejercicio 8--------------------

#triangulo de pascal
def pascal_recur(n, k):
    #k = fila n = columna
    #condicional de retorno
    if k < 2 or n == 0 or k == n:
        return 1
    #condicional de error, nunca puede ser la fila mas grande que la columna
    if n > k:
        return 0 
    #recursividad
    pascal = pascal_recur(n-1, k-1) + pascal_recur(n,k-1)
    #retornamos el resultado
    return pascal
    
print(pascal_recur(5, 10))

##--------------------Ejercicio 9--------------------

#Importo la libreria que necesito para generar número random.
import random

#Defino la función para generar todas las cadenas posibles de longitud definida por la variable "k" (permitiendo carácteres repetidos).
def combinations(list, k, current_combination=""):
    if k == 0:
        print(current_combination)
    else:
        for i in list:
            combinations(list, k - 1, current_combination + i)

#Programa Principal
#Defino la lista con los carácteres especiales.
list= ["£" , "©", "¶", "æ", "Ø"]
#Agarro un número random entre 1 y 5, y se lo asigno a la variable number, que le dará su valor a la variable llamda "k" dentro de la función "combinations".
number= random.randint(1, 5)
#Invoco la función "combinations".
combinations(list, number)

#--------------------Ejercicio 10--------------------

def paper_size_A(N):
    if N == 0:
        return (841, 1189)
    
    previous_width, previous_height = paper_size_A(N-1)
    
    current_width = previous_height // 2
    current_height = previous_width
    
    return (current_width, current_height)

N = input("Ingrese el número N de la hoja A(N) (ej: para A4 introduce 4): ")

if N.isdigit() and int(N) >= 0:
    N = int(N)
    width, height = paper_size_A(N)
    print(f"Las medidas de la hoja A{N} son: {width}mm x {height}mm.")
else:
    print("--- Ingrese un número válido ---")