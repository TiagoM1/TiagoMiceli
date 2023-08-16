# Creamos e inicializamos las variables
numero1 = 26
numero2 = 14.2
nombre = "Tiago"
nombre_mayus = "TIAGO"
apellido = "Miceli"
nombre_completo = nombre + " " + apellido
edad = 21
altura = 1.75
precio = 5900.5
descuento = 0.25
precio_final = precio * descuento
cadena = "Oferta de Alfajores"
longitud = len(cadena)

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2


# Se muestran por pantalla los valores iniciales de las variables
#  y sus modificaicones
print("-----------valores iniciales-----------")
print("numero1 = ", numero1)
print("numero2 = ", numero2)
print("nombre = ", nombre)
print("nombre en minusculas = ", nombre_mayus.lower())
print("primer letra en mayuscula= ", nombre_mayus.title())
print("apellido = ", apellido)
print("nombre_completo = ", nombre_completo)
print("edad = ", edad + 5 - 10)
print("altura = ", altura * 4 / 3)
print("precio = ", precio)
print("descuento = ", descuento)
print("precio_final = ", precio_final)
print("cadena = ", cadena)
print("longitud = ", longitud)
print("----------cambio de precio-----------")

# la variable precio cambia de valor y se muestra por consola
precio = 4800.5
print("nuevo precio = ", precio)

print("-----------operaciones----------")
# Se muestran las operaciones
print("suma = ", suma)
print("resta = ", resta)
print("multiplicacion = ", multiplicacion)
print("division = ", division)
