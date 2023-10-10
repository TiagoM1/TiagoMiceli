from TP_5_funct import *

#Ej_1

dni = input("Ingrese su DNI: ")
if(chk_dni(dni)):
    print("El DNI es válido")

#Ej_2

var = "   Texto de ejemplo   "
res = lng_word(var)
print("La longitud de la última palabra es:", res)

#Ej_3

# Inicializar un diccionario para almacenar los socios
partners = {}

while True:
    complete_name = input("Ingrese el nombre completo del socio (o nombre vacío para salir): ")
    
    if complete_name == "":
        break

    # Dividir el nombre y el DNI
    parts = complete_name.split()
    if len(parts) < 2:
        print("Formato de nombre incorrecto. Debe ingresar al menos un nombre y un apellido.")
        continue

    surname = parts[-1]
    name = " ".join(parts[:-1])

    dni = input("Ingrese el número de DNI (7 u 8 dígitos): ")
    if not check_dni(dni):
        print("Número de DNI incorrecto. Debe tener 7 u 8 dígitos.")
        continue

    # Generar el identificador
    identificator = generate_identificator(name, surname, dni)
    
    # Almacenar el socio en el diccionario
    partners[identificator] = complete_name

# Mostrar los identificadores únicos de los socios
print("Identificadores únicos de los socios:")
for identificator, name in partners.items():
    print(f"{name}: {identificator}")

#Ej_4

#Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro.

#Pide al usuario dos números enteros
num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))

if is_multiple(num1,num2):                                              #Verificar si alguno de los números es multiplo del otro
    print ("El número",num1, "es múltiplo del", num2, "o viceversa")
else:
    print ("El número",num1, "no es múltiplo del", num2, "y viceversa")

#Ej_5

i = 0
days = input("Cantidad de dias: ")
if(days.isdigit()):
    days = int(days)
    
    while i < days:
        
        print("\nDia: " + str(i+1))
        min = input("Temperatura minima: ")
        max = input("Temperatura maxima: ")
        if(min.isdigit() and max.isdigit()):
            i += 1
            min = int(min)
            max = int(max)
            if(min > max):
                aux = max
                max = min
                min = aux

            print(f"Temperatura promedio: " + average_temperature(min,max))
        else:
            print("--- Ingrese numeros, intente denuevo ---")
else:
    print("--- Ingresaste cualquier cosa ---")

print("-- PROGRAMA FINALIZADO --")

#Ej_6

text= input("Ingrese un texto o palabra: ")
print(spacer(text))

#Ej_7

min_max()   

#Ej_8

radio = int(input("Ingrese el radio del circulo: "))

calc_area_perimetro(radio)

#Ej_9

test = 0  # Inicializamos el número de intentos a 0

while test < 3:  # Permitimos un máximo de 3 intentos
    user = input("Ingrese nombre de usuario: ")
    passw = input("Ingrese contraseña: ")

    result, test = login(user, passw, test)

    if result:
        print("¡Login exitoso!")
        break
    else:
        print("Login fallido. Intento {}/3".format(test))

if test >= 3:
    print("Se ha excedido el número máximo de intentos. Bloqueando el acceso.")

#Ej_10 

# Obtener carrito y descuentos del usuario
cart, discounts = cart_and_discounts()

# Calcular el precio total con descuento
total_price = apply_discounts(cart, discounts)

# Mostrar el precio total
print("Precio total con descuento:", total_price)

#Ej_11

#Escribir una función que reciba otra función y una lista, y devuelva otra lista con el resultado de aplicar la función dada a cada uno de los elementos de la lista.

numbers = [1,2,3,4,5]       #Crear una lista de números

result = apply_function(square, numbers)    #Aplicar la función cuadrado a cada elemento de la lista

print(result)               #Imprimir el resultado

#Ej_12

dictionary:{}
frase = input("Ingrese una frase: ")
aux = ""

print("diccionario:", frase_counter(frase, dictionary, aux))

#Ej_13

vector_modulus_calculator()

#Ej_14

num = int(input("Ingrese número positivos para saber si es primo  \n> "))

if prime_num(num):
    print(f"{num} es un número primo")
else:
    print(f"{num} no es un número primo")

#Ej_15

factorial_num()

#Ej_16

# Solicitar al usuario un número entero
strnumb = input("Ingrese un número entero: ")

if whol_num(strnumb):
    numb = int(strnumb)
    dig = input("Ingrese un dígito: ")          # Solicitar al usuario un dígito

    if dig_func(dig):
        frqncy = freq(numb, dig)
        print(f"El dígito {dig} aparece {frqncy} veces en el número {numb}.")
    else:
        print("Debe ingresar un solo dígito válido.")
else:
    print("Debe ingresar un número entero válido.")

#Ej_17

mayor_primo = 0

while True:
    try:
        numero = int(input("Ingrese un número primo (o un número no primo para finalizar): "))
        
        if not es_primo(numero):
            break

        if numero > mayor_primo:
            mayor_primo = numero

        suma = suma_digitos(numero)
        print(f"La suma de los dígitos es: {suma}")

        digito = int(input("Ingrese un dígito para contar su frecuencia en el número: "))
        frecuencia = contar_digitos(numero, digito)
        print(f"El dígito {digito} aparece {frecuencia} veces en el número.")

    except ValueError:
        print("Ingrese un número válido.")

if mayor_primo > 0:
    resultado_factorial = factorial(mayor_primo)
    print(f"El factorial del mayor número primo ingresado ({mayor_primo}) es: {resultado_factorial}")
else:
    print("No se ingresaron números primos.")