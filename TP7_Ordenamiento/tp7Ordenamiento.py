##--------------------Ejercicio 1--------------------

#Función para ordenar la lista con el método de ordenamiento de Bubble Sort
def bubble_ord(list):
    for i in range(len(list)):
        for j in range(0, len(list) - i - 1):
            if (list[j] > list[j+1]):
                helper= list[j+1]
                list[j+1]= list[j]
                list[j]= helper
    return list

#Programa principal
#Defino la lista e imprimo la misma pero ordenada, uando la funcion creada anteriormente
random_list= [5, 1, 3, 2, 4, 8, 6, 9, 7]
print("Lista ordenada Menor -> Mayor (Bubble Sort):")
print(bubble_ord(random_list))

#--------------------Ejercicio 2--------------------

#Debo realizar una funcion que reciba una lista de palabras y ordenarla alfabeticamente

#Creo la funcion que funcionara de forma recursiva
def ord_alph(array):
    abc = "abcdefghijklmnñopqrstuvwxyz"      
    
    #creo uan lista vacia
    num_list = [0]*len(array)       

    #relleno la lista con el número de la posicion que le corresponde en el abecedario
    for i in range(len(array)):
        num_list[i] = abc.index(array[i][0])

    #Ordeno la lista de palabras en funcion al orden de la otra listra creada con las posiciones, en orden ascendente
    for i in range(len(num_list)):
        low = i
        for j in range(i,len(num_list)):
            if num_list[j] < num_list[low]:
                low = j
        if i!= low:
            num_list[i], num_list[low] = num_list[low], num_list[i]
            array[i], array[low] = array[low], array[i]

    #Repito esta secuencia hasta que se ordenen las palabras que tienen coincidencias con sus primeras letras
    while True:
        number = -2

        #identifico si se repiten palabras
        for i in range(len(num_list)-1):
            if num_list[i] ==  num_list[i+1]:
                number = num_list[i]
                break
        
        #Retorna la lista cuando ya esta todo ordenado
        if number == -2:
            return array
        #En caso de que haya coincidencias de letras 
        else:
            cant = num_list.count(number)
            loc = num_list.index(number)
            #Agarro el par de palabras que empicen igual
            list_2 = array[loc:loc+cant]

            #Les quito la primera letra
            for i in range(len(list_2)):
                list_2[i]= list_2[i][1:]

            #ahora lo ordeno de forma recursiva, y en cada llamado le quita una letra hasta que dejen de haber coincidencias
            list_2 = ord_alph(list_2)

            #agrego el nuevo orden de palabras a la lista principal, y le cambio el número de posicion para que sea unico y no haya coincidencias despues
            for i in range(len(list_2)):
                array[loc+i] = array[loc][0]+list_2[i]
                num_list[loc+i] = number + i/10

word_list = ["sandia", "mono", "manco", "miel", "rolex", "puerro", "montura", "miedo", "mirada"]

#Convierto todas las palbras en minúsculas
for elem in word_list:
    elem = elem.lower()

print(f"Lista de palabras: {word_list}")

list_order = ord_alph(word_list)

print(f"Lista ordenada alfabeticamente: {list_order}")

#--------------------Ejercicio 3--------------------

libros = [
    {"título": "Cien años de soledad", "autor": "Gabriel García Márquez", "año": 1967},
    {"título": "Geronimo Stilton", "autor": "Elisabetta Dami", "año": 2000},
    {"título": "Un mundo feliz", "autor": "Aldous Huxley", "año": 1932},
    {"título": "Cartas a Lucilio", "autor": "Seneca", "año": 1494},
    {"título": "Tu Súper Cerebro", "autor": "Kaja Nordengen", "año": 2019},
]

def ordenar_libros(lista, campo):
    return sorted(lista, key=lambda x: x[campo])

# Ordenar libros por año de publicación
libros_ordenados_por_año = ordenar_libros(libros, "año")
for libro in libros_ordenados_por_año:
    print(libro)

print("\n")

# Ordenar libros por autor
libros_ordenados_por_autor = ordenar_libros(libros, "autor")
for libro in libros_ordenados_por_autor:
    print(libro)

#--------------------Ejercicio 4--------------------

def insertion_sort(strings):                                    #Funcion para el metodo de ordenamiento de inserción
    for i in range(1, len(strings)):
        current_string = strings[i]
        j = i - 1

        while j >= 0 and len(current_string) < len(strings[j]):
            strings[j + 1] = strings[j]
            j -= 1

        strings[j + 1] = current_string

strings = ["Programación", "Python", "Código", "Messi", "Java", "Developer"]      #Lista de cadenas de entrada

insertion_sort(strings)                                   #Llamar a la función de ordenamiento de inserción

print("Lista ordenada por longitud de cadena (ascendente):")    #Imprimir la lista ordenada
for string in strings:
    print(string)

#--------------------Ejercicio 5--------------------

def insertion_sort_decendent(strings):
    for i in range(1, len(strings)):
        current_string = strings[i]
        j = i - 1
        #Igual al ejercicio 4 pero simplemente cambia el signo, en vez de insertarlo como primero cuando sea menor, lo insertamos cuando sea mayor
        while j >= 0 and len(current_string) > len(strings[j]):
            strings[j + 1] = strings[j]
            j -= 1
        strings[j + 1] = current_string

strings = ["Python", "Código", "Messi", "t","Programación", "Java", "Developer", "testeo300"]     

insertion_sort_decendent(strings)                                 

print("Lista ordenada por longitud de cadena (ascendente):")   
for string in strings:
    print(string)

#--------------------Ejercicio 6--------------------

#Escribe un programa que tome una lista de números enteros y ordene la lista utilizando el algoritmo de ordenamiento por conteo.

def counting_sort(arr):
    max_val = max(arr)
    min_val = min(arr)
    range_val = max_val - min_val + 1

    # Crear una lista de conteo para almacenar la frecuencia de cada número
    count = [0] * range_val

    # Contar la frecuencia de cada número en la lista original
    for num in arr:
        count[num - min_val] += 1

    # Reconstruir la lista ordenada
    sorted_arr = []
    for i in range(range_val):
        for j in range(count[i]):
            sorted_arr.append(i + min_val)

    return sorted_arr

disord_list = [4, 2, 2, 8, 3, 3, 1]
ord_list = counting_sort(disord_list)
print("Lista ordenada:", ord_list)

#--------------------Ejercicio 7--------------------

# Crear una lista con números y cadenas de caracteres
mixed_list = [5, 'tarea', 2, 'universidad', 8, 'scrum', 1, 'master']

# Separar los números y las cadenas en listas separadas
numbers = [x for x in mixed_list if isinstance(x, int)]
strings = [x for x in mixed_list if isinstance(x, str)]

# Ordenar las listas
numbers.sort()
strings.sort()

# Combinar las listas ordenadas
sorted_list = numbers + strings

# Imprimir la lista ordenada
print(sorted_list)

#--------------------Ejercicio 8--------------------

def merge_sort(arr):                                    #Funcion para aplicar el metodo Merge Sort
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

input_numbers = [38, 27, 43, 3, 9, 82, 18, 21, 81, 40, 14]      #Lista de números

merge_sort(input_numbers)                                       #Llamada a la función

print("Lista ordenada utilizando Merge Sort:")                  #Imprime la cadena ordenada
print(input_numbers)