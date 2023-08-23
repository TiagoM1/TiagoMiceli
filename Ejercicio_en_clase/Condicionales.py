fecha = ""
i = 0
dia = ""
dd = 0
mm = 0
aprobados = 0
desaprobados = 0
asistencia = 0
cant_alumnos = 0
arancel = 0

print("Ingrese la fecha en este formato: dia,dd/mm")
fecha = input("Fecha: ")
#Se guarda la posción de cada caracter
coma = fecha.find(",")
barra = fecha.find("/")

# Se extraer los datos de la fecha y se les asigna al tipo de variable correspondiente
dia = fecha[:coma]
dd = int(fecha[coma + 1:barra])
mm = int(fecha[barra + 1:])

# Filtro de dd
if dd < 1 or dd > 31:
    print("Error en dia")
    quit()

#Filtro de mm
if mm < 1 or mm > 12:
    print("Error en mes")
    quit()

#Filtro de dia
if dia == "lunes" or dia == "martes" or dia == "miercoles":
    aprobados = int(input("N° alumnos aprobados en el examen: "))
    desaprobados = int(input("N° alumnos desaprobados en el examen: "))
    print(f"Porcentaje de aprobados: {round((aprobados * 100) / (aprobados + desaprobados))} %")
elif dia == "jueves":
    asistencia = int(input("Porcentaje de asistencia: "))
    if asistencia > 51:
        print("Asistió la mayoría")
    else:
        print("No asistió la mayoría")
elif dia == "viernes":
    if (dd == 1 and (mm == 1 or mm == 7)):
        print("Comienza un nuevo ciclo")
        cant_alumnos = int(input("Cantidad de alumnos: "))
    arancel = int(input("Valor del arancel: "))
    if cant_alumnos > 0:
        print(f"Total del ingreso: {arancel * cant_alumnos} $")
    else:
        print("No se ingresó la cantidad de alumnos")
else:
    print("El día " + dia + " no existe")
    quit()

'''
Un instituto de inglés necesita un programa que le permita, cada día, procesar
observaciones sobre las clases de ese día. El instituto dicta clases a estudiantes de
distintos niveles y cada nivel tiene clases en un día de la semana diferente: 
los lunes se dicta nivel inicial, los martes el nivel intermedio, los miércoles el nivel avanzado,
los jueves son para práctica hablada y los viernes se dicta inglés para viajeros.

Se debe comenzar por solicitar al usuario que ingrese la fecha actual en formato “día,
DD/MM”, donde [día] es un día de la semana, DD es el número de día y MM es el
número de mes. Si el usuario ingresa un día de la semana inexistente o una fecha cuyo
día supere el número 31 o el mes supere el número 12, finalizar el programa indicando
que se produjo un error. 
Debe permitirse que ingrese el día de la semana en
minúsculas o mayúsculas indistintamente. Como precondición se tiene que lo
ingresado por el usuario tendrá la forma <[alfanumérico], [numérico]/[numérico]>.

Una vez indicada la fecha el usuario necesita poder indicar si ese día se tomaron los
exámenes, pero eso solo si se trata de los niveles inicial, intermedio o avanzado, ya
que las prácticas habladas y el inglés para viajeros no tienen exámenes. 
Si hubo
exámenes, el usuario ingresará cuántos alumnos aprobaron y cuantos no, y el
programa le mostrará el porcentaje de aprobados.
Si el día fue el correspondiente a práctica hablada, el usuario deberá ingresar el
porcentaje de asistencia a clase y el programa le indicará ‘asistió la mayoría’ en caso de
que la asistencia sea mayor al 50% o ‘no asistió la mayoría’ si no es así.

Si se trata del inglés para viajeros y la fecha actual corresponde al día 1 del mes 1 o del
mes 7, se deberá imprimir ‘Comienzo de nuevo ciclo’ y solicitar al usuario que ingrese
la cantidad de alumnos del nuevo ciclo y el arancel en $ por cada alumno, para luego
imprimir el ingreso total en $.
'''