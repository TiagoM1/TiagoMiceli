
# Ejercicio 1
base = float(input("Ingrese la base: "))
altura = float(input("Ingrese la altura: "))
area_rectangulo = base * altura
perim_rectangulo = (base * 2) + (altura * 2)
print(
    f"área del rectángulo:  {area_rectangulo}.\nPerimetro del Rectángulo: {perim_rectangulo}")

# Ejercicio 2
cateto1 = float(input("Ingrese el valor del cateto 1: "))
cateto2 = float(input("Ingrese el valor del cateto 2: "))
hipotenusa = ((cateto1*2)+(cateto2))*(1/2)
print("La hipotenusa del triángulo es: ", hipotenusa)


# Ejercicio 3
num1 = float(input('ingrese el primer numero '))
num2 = float(input('ingrese el segundo número '))
suma = num1+num2
print(suma)
resta = num1-num2
print(resta)
multiplicacion = num1*num2
print(multiplicacion)
division = num1/num2
print(division)

# Ejercicio 4

farenh = float(input("Ingrese los grados fahrenheit: "))
celsius = (farenh-32)*5/9
print(f"El equivalente en celsius de {farenh}°F es: {celsius}°C")


# Ejercicio 5


# a) A = input(nombre, “¿Cuál es tu canción favorita?”)
# El error se encuentra en que input no puede recibir dos argumentos
# Solucion: Sacando la variable "nombre"

# b)	precio = input(“Precio: “)
# total = precio + (precio * 0.1)
# El error se encuentra en que input devuelve una string,
# y una string no puede ser multiplicada, ni ser sumada a otros numeros
# Solucion: usando int en el input, quedando: int(input("Precio: "))

# c)	edad = int(input(“Edad: “))
# print(tu edad es, edad)
# El error esta en el print, el cual no tiene "" representando una string,
# baisamente le esta pasando de forma erronea los argumentos
# Solucion: agregando comillas de esta forma: print("tu edad es", edad)

# d)	edad = int(input(“Edad: “))
# print(“Veamos si tu edad es 18…”, edad=18)
# El error esta en que no es valido el argumento que se le pasa, "edad=18", ademas de que un solo igual
# representa asignacion.
# La solucion seria usar un if else, con la condicion "edad==18"
# algo asi:
# edad = int(input("Edad: "))
# if edad == 18:
#  print("Veamos si tu edad es 18… Tienes 18 años")
# else:
#   print("tu edad no es 18 años")

# Ejercicio 6
num = 0
suma = 0
for i in range(3):
    num = float(input(f"Ingrese la el numero {i+1}: "))
    suma = suma + num
print(f"Media: {suma/3}")


# Ejercicio 7

valor = int(input("Ingrese la cantidad de minutos que desee: "))

minutos = valor % 60
horas = (valor - minutos)/60
print(f"{valor} minutos son {horas} horas y {minutos} minutos")


# Ejercicio 8

sueldo_base = float(input("Ingrese el sueldo base: "))
# cantidad_ventas = int(print("Ingrese cantidad de ventas:) "))
cantidad_ventas = 3
comision = 0.1*cantidad_ventas*sueldo_base
sueldo_total = sueldo_base + comision
print(
    f"Total de dinero en comisiones $ {comision} \nRemuneracion total de salario mas comision es: ${sueldo_total}")

# Ejercicio 9
compra = float(input("Ingrese el valor de su compra: "))
descuento = 0.15
total = compra-(compra*descuento)
print("El total de su compra con descuento es de: ", total)


# Ejercicio 10
parcial1 = float(input('ingrese la nota del primer parcial: '))
parcial2 = float(input('ingrese la nota del segundo parcial: '))
parcial3 = float(input('ingrese la nota del tercer parcial: '))

notas_parcial = (parcial1+parcial2+parcial3)/3

examen_final = float(input('ingrese la nota del examen final: '))

trabajo_final = float(input('ingrese la nota del trabajo final: '))

promedio = (notas_parcial * 0.55) + \
    (examen_final * 0.30) + (trabajo_final * 0.15)

print('el promedio de todas tus notas es de: ', promedio)

# Ejercicio 11.

num1 = float(input("Ingrese numero 1: "))
num2 = float(input("Ingrese numero 2: "))

dist = abs(num1 - num2)

print(f"La distancia entre {num1} y {num2} es: {dist}")


# Ejercicio 12

numero = float(input("Ingrese un numero: "))

r_cuadrada = numero**1/2
r_cubica = numero**1/3

print(
    f"La raiz cuadrada de {numero} es: {r_cuadrada} y su raiz cubica es: {r_cubica}")

# Ejercicio 13
num = input("Ingrese un número:")
inversa = ""
for i in range(len(num)):
    inversa += num[len(num) - 1 - i]
print(f"num: {num}")
print(f"Inversa: {inversa}")


# Ejercicio 14

numero_a = int(input("Ingrese el primer número que desee: "))
numero_b = int(input("Ingrese el segundo número que desee: "))

numero_h = numero_a
numero_a = numero_b
numero_b = numero_h
print(
    f"El primer número ingresado cambió a {numero_a} y el segundo número ingresado cambió a {numero_b}")


# Ejercicio 15
hora_inicial = int(input("Ingrese la hora de salida: "))
minuto_inicial = int(input("ingrese el minuto de salida: "))
segundo_inicial = int(input("ingrse el segundo de salida: "))
tiempo_viaje = int(input("Ingrese en segundos el tiempo de viaje: "))
horas = tiempo_viaje//3600
minutos = (tiempo_viaje % 3600)//60
segundos = tiempo_viaje % 60
segundo_final = (segundo_inicial + segundos) % 60
minuto_final = (minuto_inicial + (segundo_inicial + segundos)//60+minutos) % 60
hora_final = (hora_inicial+horas+(minuto_inicial +
              (segundo_inicial + segundos)//60+minutos)//60) % 24
print(
    f"Hora de salida:   {hora_inicial} hs  {minuto_inicial} min {segundo_inicial} seg")
print(
    f"Hora de llegada:   {hora_final} hs {minuto_final} min {segundo_final} seg")

# Ejercicio 16
nombre = input("Ingrese su nombre: ")
apellido1 = input("Ingrese su primer apellido: ")
apellido2 = input("Ingrese su segundo apellido: ")
iniciales = nombre[0], apellido1[0], apellido2[0]
print("Sus iniciales son: ", iniciales)


# Ejercicio 17
usuario = input('ingrese su nombre: ')
print('ahora estás en la matrix, ', usuario)

# Ejercicio 18

valor_cena = float(input("Ingrese el valor de la cena: "))
cost_serv = (valor_cena * 6.2)/100
propi = (valor_cena * 10)/100
print(
    f"El valor de la cena, sumando el costo de servicio y la propina es: {valor_cena + cost_serv + propi}")


# Ejercicio 19

dia = int(input("Ingrese el dia de tu nacimiento: "))
mes = int(input("Ingrese el mes de tu nacimiento: "))
año = int(input("Ingrese el año de tu nacimiento: "))

print(f"El dia de tu nacimiento es: {dia}/{mes}/{año}")

# Ejercicio 20
fecha = ""
fecha = input("Día de Nacimiento: ")
fecha += input("Mes de Nacimiento: ")
fecha += input("Año de Nacimiento: ")
print(f"Fecha: {fecha}")


# Ejercicio 21

km_1litro = int(input(
    "Ingrese la cantidad kilómetros que su moto recorre con 1L de combustible: "))
capacidad = int(
    input("Ingrese la cantidad de litros que posee su tanque de combustible: "))
trayecto = int(input("Ingrese la cantidad de kilometros que desea recorrer: "))
km_tanque = 0
t_requeridos = 0

# Calculo la cantidad de kilómetros que hago con un solo tanque
km_tanque = km_1litro*capacidad
# Calculo los tanques necesarios para el trayecto deseado y lo redondeo
t_requeridos = trayecto/km_tanque
t_requeridos = round(t_requeridos)
print(
    f"Usted necesitará {t_requeridos} tanques de conbustible para realizar los {trayecto}Km deseados.")

'''
6-13-20
1.	Calcular el perímetro y área de un rectángulo dada su base y su altura.

2.	Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

3.	Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.

4.	Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius. Recordar que la fórmula para la conversión es:

 
5.	¿Qué problemas tienen las siguientes instrucciones?¿Cómo las solucionarías?

a)	A = input(nombre, “¿Cuál es tu canción favorita?”)
b)	precio = input(“Precio: “)
total = precio + (precio * 0.1)
c)	edad = int(input(“Edad: “))
print(tu edad es, edad)
d)	edad = int(input(“Edad: “))
print(“Veamos si tu edad es 18…”, edad=18)

6.	Calcular la media de tres números pedidos por teclado.

7.	Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde. Por ejemplo: 1000 minutos son 16 horas y 40 minutos.

8.	Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.

9.	Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto deberá pagar finalmente por su compra.

10.	Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes:
•	    55% del promedio de sus tres calificaciones parciales.
•	    30% de la calificación del examen final.
•	    15% de la calificación de un trabajo final.

11.	Pide al usuario dos números y muestra la “distancia” entre ellos (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).

12.	Realizar un algoritmo que lea un número y que muestre su raíz cuadrada y su raíz cúbica.

13.	Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido. Ejemplo, si se introduce 23 que muestre 32.

14.	Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo que intercambie los valores de ambas variables y muestre cuanto valen al final las dos variables.

15.	Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. Escribir un algoritmo que determine la hora de llegada a la ciudad B.

16.	Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.

17.	Solicitar al usuario que ingrese su nombre. El nombre se debe almacenar en una variable llamada usuario. A continuación mostrar por pantalla: “Ahora estás en la matrix, [nombre del usuario]”.

18.	Hacer un programa que solicite al usuario cuánto costó una cena en un restaurante. A ese valor, sumarle un 6.2% en concepto de servicio y un 10% de propina. Imprimir en pantalla el monto final a pagar.

19.	Solicitar al usuario que ingrese el día, mes y año de su nacimiento y almacenar cada uno de ellos en una variable numérica (en total, tres variables diferentes). Finalmente, mostrar la fecha en formato dd/mm/aaaa.

20.	Hacer otra versión del programa, pero esta vez almacenado todo en una única variable con formato DDMMAAA.

21.	Una pareja de motociclistas necesita hacer ciertos cálculos antes de emprender un viaje en moto, para saber cuántos tanques de combustible consumirá el viaje entero.
Para eso deben ingresar: cuántos kilómetros puede recorrer su moto con 1 litro de combustible, qué capacidad (en litros) tiene el tanque y cuántos kilómetros en total recorrerán.
Hacer un programa que solicite los datos necesarios y luego informe la cantidad de tanques de combustible necesarios.



'''
