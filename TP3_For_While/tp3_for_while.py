#--------TP 3 For-While---------


#Ejercicio 1

word = str(input("Ingrese una palabra: "))
for i in range(10):
    print(word)


#Ejercicio 2

age = int(input("Edad: "))
for i in range(1, age + 1):
    print(i)


#Ejercicio 3

num=int(input('Ingrese un numero: '))
if num < 1:
    print('Ingrese un numero positivo')
else:
    impares=[str(i) for i in range(1,num + 1) if i%2 == 1]
    resultado=impares
print('Los numeros impares a partir de 1 son: ',resultado)


#Ejercicio 4

num_ingresado = int(input("Ingrese un numero entero positivo: "))
coma = ", "
num = ""
while num_ingresado >= 0:
    if num_ingresado !=0:
        nuevo_num = str(num_ingresado) + coma
        num = num + nuevo_num
        num_ingresado -=1
    else:
        nuevo_num = str(num_ingresado)
        num = num + nuevo_num
        num_ingresado -=1
print(num)


#Ejercicio 5

dinero = float(input("Ingrese la cantidad de dinero a invertir: "))
interes_anual = float(input("ingrese el interes anual como decimal: "))
n_anos = int(input("Ingrese el numero de años: "))
capital_total = 0
i = 0
anual_temp = 0
while i < n_anos:
    anual_temp = dinero * (1 + interes_anual/1)*(1(i+1))
    print((1 + interes_anual/1)*1(i+1))
    print(f"En el año: {i}, obtendras una cantidad de: ${anual_temp} dinero")
    i += 1
print(f"En la cantidad de tiepo {n_anos}, obtendras una inversion de: ${anual_temp}")


#Ejercicio 6

value= int(input("Por favor, ingrese un número entero: "))
chain= ""
i= 0

while i < value:
    chain+= "*"
    i+= 1
    print(chain)


# Ejercicio 7 

for i in range(1,11):
    for j in range(1,11):
        tabl = i*j
        print(f'{i}x{j}={tabl}')


#Ejercicio 8

num=int(input("Ingrese un numero entero: "))

for i in range(1,6):
    print(f'{num}' * i)


#Ejercicio 9

password= input("Por favor, ingrese su contraseña: ")
confirm_pass= input("Por favor, repita su contraseña para confirmarla: ")

while confirm_pass != password:
    confirm_pass= input("Contraseña incorrecta, por favor, inténtelo de nuevo: ")

print("Contraseña guardada con éxito")


#Ejercicio 10

numero = float(input("Ingrese el numero para saber si es primo o no: "))
if numero <= 1:
     print("No es primo")
elif numero <= 3:
     print("Es primo")
elif numero % 2 == 0 or numero % 3 == 0:
    print("No es primo")
else:
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            print("No es primo")
            break  
        i += 6
    else:
        print("Es primo")


#Ejercicio 11

palabra = input("Ingrese una palabra: ")
sum=0
for letra in palabra:
    sum+=1
while sum > 0:
    letras = palabra[sum-1]
    sum-=1
    print(letras)


#Ejercicio 12

frase=input('Ingrese una frase: ')
letra=input('Ingrese una letra: ')
contador=0
for caracter in frase:
    if caracter.lower()==letra.lower():
        contador+=1
print('La letra ingresada aparece', contador,'veces en la frase',frase)


#Ejercicio 13

word = ""
while word != "salir":
    word = input("Palabra: ").lower()
    if word != "salir":
        print(word)
        print("   " + word)
        print("      " + word)

print("--- se derrumbo la cueva, no más eco ---")


#Ejercio 14

#La siguiente instruccion pedira 2 numros al usuario, entonces habrá que imprimir que números son pares o impares, entre el rango del primer número hasta el segundo
num1 = int(input("Ingrese un número entero: "))
num2 = int(input("Ingrese otro número entero: "))
if num1<num2:                       #Comparo cual número es mayor asi ubico los valores del range()
    for i in range(num1, num2+1):   #Si num1 es menor ira primero en el parametro de range()
        if i%2==0:                  #Comprebo si es par o impar y lo imprimo en pantalla
            print(f"{i} es par")
        else:
            print(f"{i} no es par")
else:
    for i in range(num2, num1+1):   #Si num1 es mayor irá segundo en el orden de parámetros de range
        k = ((num1+num2)-i)         #Creo otra varible para que el contador sea de forma decendiente
        if k%2==0:                  #Comprebo si es par o impar y lo imprimo en pantalla
            print(f"{k} es par")
        else:
            print(f"{k} no es par")


#Ejercicio 15

#Se me solicita que imprima todos los divisores de un numero ingresado por el usuario
dividers = []
num = -1

#verifico que el numero sea válido
while num<=0:           
    num = int(input("Ingrese un número entero mayor que cero: "))
    if num<=0:
        print("número inválido")

#Al numero ingresado lo divido por cada numero desde el 0 hasta si mismo los que dan de resto cero son sus divisores, y   
for i in range(num+1):
    if num%(i+1) == 0:
        dividers.append(i+1)    #Los que dan de resto cero son sus divisores, se agregan a una lista 
    else:
        continue

print(f"Los divisores de {num} son: ") #Recorro la lista para imprimir cada divisor

for k in dividers:
    if k == num:
        print(k)
    else:
        print(k, end=", ")


#Ejercicio 16

negative = 0
amount = int(input("Cantidad de números a ingresar: "))
if amount > 0:
    for i in range(amount):
        num = int(input("num: "))
        if num < 0:
            negative += 1
    print(f"Cantidad de numeros negativos: {negative}")
else:
    print("Debe ser mayor a cero")


#Ejercicio 17

frase=input('Ingrese una frase: ')
abc='aeiouAEIOU'
vocales=[]
for caracter in frase:
    if caracter in abc and caracter not in vocales:
        vocales += caracter
print(vocales)


#Ejercicio 18

num1=0
num2=1
for n in range(10):
    num3 = num1 + num2
    num1 = num2
    num2 = num3
    print(num3)
    

#Ejercicio 19

objetivo = float(input("Ingrese la cantidad de dinero como objetivo a ahorrar: "))
ahorro = 0
while ahorro < objetivo:
    dinero = float(input("Ingrese la cantidad de dinero a ahorrar: "))
    if dinero < 0:
        print("Por Favor ingrese un numero positivo")
    else:
        ahorro += dinero  
    faltante = objetivo - ahorro 
    if faltante <= 0:
        print(f"Ah llegado al objetivo!!! Felicidades!!!, a ahorrado un total de {ahorro}, superando el objetivo de: {objetivo}")
    else:
        print(f"Actualmente a ahorrado: {ahorro}, le faltarian un total de: {faltante} para lograr el objetivo")


#Ejercicio 20

number= ""
add= 0

while number != 0:
    number= int(input("Por favor, ingrese un número entero: "))
    add+= number
print(f"La suma de todos los número ingresados es {add}")


#Ejercicio 21

maximo = None
while True:
    numero = int(input("Ingrese un número entero positivo (0 para salir): "))
    
    if numero == 0:
        break

    if maximo is None or numero > maximo:
            maximo = numero
if maximo is not None:
    print(f"El número máximo ingresado fue: {maximo}")


#Ejercicio 22

num_pares=0
while True:
    numero= int(input("Ingresa un número entero positivo(-1 para salir): "))

    if numero == -1:
        break

    suma_num=str(numero)
    suma_digitos=0
    for digito in suma_num:
        suma_digitos+=int(digito)
    print(f'la suma de sus digitos es : {suma_digitos}')
    if numero % 2 ==0:
        num_pares+=1
print(f'la cantidad de numeros pares es: {num_pares}')


#Ejercicio 23

buys= int(input("Por favor, ingrese el monto de su compra: "))
values= []
iterator= 0

while buys != 0:
    values.append(buys)
    print("-----------------------------------")
    buys= int(input("Ingrese su siguiente monto: "))

for iterator in values:
    print(f"{iterator}; ", end=' ')


#Ejercicio 24

buys= int(input("Por favor, ingrese el monto de su compra: "))
suma_montos= buys
while suma_montos != 0:
    print("-----------------------------------")
    monto = int(input("Ingrese su siguiente monto: "))
    if monto < 0:
        print("Vuleva a ingresar un nuevo monto")
        continue
    elif monto == 0:
        break
    suma_montos += monto
if suma_montos > 1000:
    descuento = (suma_montos * 10) / 100
    total = suma_montos - descuento
    print("-----------------------------------")
    print(f"El total a pagar es de: ${suma_montos}, con un descuento del 10% le quedaria en: {total}")
else:
    print("-----------------------------------")
    print(f"El total a pagar es de: ${suma_montos}")


#Ejercicio 25

num1= int(input("Ingrese un numero entero positivo: "))
num2= 1
n= 0
while n < num1:
    n+=1
    num2 = num2*n
print("El factorial de",num1,"es",num2)


""" 2 - 13 - 16
1-	Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

2-	Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

3-	Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

4-	Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

5-	Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

6-	Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
 
7-	Escribir un programa que muestre por pantalla las tablas de multiplicar del 1 al 10.

8-	Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
 
9-	Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

10-	Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

11-	Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

12-	Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.

13-	Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.

14-	Escriba un programa que pida dos números enteros y escriba qué números son pares y cuáles impares desde el primero hasta el segundo.

15-	Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores.

16-	Escriba un programa que pregunte cuántos números se van a introducir, pida esos números y escriba cuántos negativos ha introducido.

17-	Solicitar al usuario que ingrese una frase y luego imprimir un listado de las vocales que aparecen en esa frase (sin repetirlas).

18-	Crear un algoritmo que muestre los primeros 10 números de la sucesión de Fibonacci. La sucesión comienza con los números 0 y 1 y, a partir de éstos, cada elemento es la suma de los dos números anteriores en la secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…

19-	Escriba un programa que simule una alcancía. El programa solicitará primero una cantidad, que será la cantidad de dinero que queremos ahorrar. A continuación, el programa solicitará una y otra vez las cantidades que se irán ahorrando, hasta que el total ahorrado iguale o supere al objetivo. El programa deberá comprobar que las cantidades ingresadas sean positivas.

20-	Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.

21-	Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.

22-	Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen. La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.

23-	Crear un programa que permita al usuario ingresar los montos de las compras de un cliente (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0.

24-	Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.

25-	Dado un número entero positivo, mostrar su factorial. El factorial de un número se obtiene multiplicando todos los números enteros positivos que hay entre el 1 y ese número. El factorial de 0 es 1.


"""
