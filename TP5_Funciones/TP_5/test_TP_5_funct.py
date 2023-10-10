import pytest
from TP_5_funct import *

#Ej_1

@pytest.mark.parametrize("a,res",[
    (12345678, True),
    (1234567, True),
    (2222222222, False),
    (33.3, False),
    (12245679, True),
    (45137598, True),

])
def test_chk_dni(a,res):
    assert chk_dni(a) == res

#Ej_2

def test_lng_word():
    assert lng_word("Hello World") == 5
    assert lng_word("Python") == 6
    assert lng_word("") == 0
    assert lng_word("   ") == 0

#Ej_3

def test_check_dni():
    assert check_dni("12345678") == True

def test_generate_identificator():
    assert generate_identificator("John Doe", "Smith", "12345678") == "John5123"

#Ej_4

def test_is_multiple():
    assert is_multiple(10, 2) == True
    assert is_multiple(10, 3) == False
    assert is_multiple(0, 5) == True
    assert is_multiple(7, 0) == False
    assert is_multiple(0, 0) == False

#Ej_5

def test_average_temperature():
    assert average_temperature(10, 20) == "15.0"
    assert average_temperature(0, 0) == "0.0"
    assert average_temperature(-10, 10) == "0.0"
    assert average_temperature(10, 20) == "15.0"

#Ej_6

def test_spacer():
    assert spacer("5") == "Ingrese solo letras, por favor."

#Ej_7

#def min_max():

#Ej_8

@pytest.mark.parametrize("b,area_res, perimetro",[
    (12, "75.40", "452.39"),
    ("3", "18.85", "28.27" ),
    (4, "25.13", "50.27"),
    (6, "37.70", "113.10" ),

])
def test_calcular_Area_Perimetro(b,area_res, perimetro):
    per, area = calc_area_perimetro(b)
    assert area == area_res
    assert per == perimetro

#Ej_9

def test_login():
    assert login("usuario1", "asdasd", 0) == (True, 0)
    assert login("usuario2", "wrong_password", 0) == (False, 1)
    assert login("usuario1", "asdasd", 1) == (True, 1)

#Ej_10

#def apply_discounts():
#def cart_and_discounts():

#Ej_11

def test_apply_function():
    assert apply_function(square, [1, 2, 3, 4, 5]) == [1, 4, 9, 16, 25]
    assert apply_function(square, [1, 2, 3]) == [1, 4, 9]

#Ej_12

def test_frase_counter():
    dictionary = {}
    aux = ""
    assert frase_counter("Hola mundo", dictionary, aux) == {'Hola': 4, 'mundo': 5}

#Ej_13

def test_vector_modulus_calculator():
    assert vector_modulus_calculator(3, 4) == 5.0

#Ej_14

def test_prime_num():
    assert prime_num(2) == True
    assert prime_num(4) == False
    assert prime_num(17) == True
    assert prime_num(0) == False

#Ej_15

@pytest.mark.parametrize("c,res,salir",[
    (0, 1, "si"),
    (1, 1, "si"),
    (6, 720, "si"),

])
def test_factorial_de_numero(c,res, salir):
    assert factorial_num(c, salir) == res

#Ej_16

def test_freq():
    assert freq(1223334444, '2') == 2
    assert freq(123456789, '0') == 0
    assert freq(-11223344, '1') == 2

def test_whol_num():
    assert whol_num("12345") == True
    assert whol_num("-12345") == True
    assert whol_num("12a34") == False
    assert whol_num("0") == True

def test_dig_func():
    assert dig_func("5") == True
    assert dig_func("a") == False
    assert dig_func("123") == False 

#Ej_17

def test_es_primo():
    assert es_primo(2) == True
    assert es_primo(4) == False
    assert es_primo(17) == True
    assert es_primo(0) == False

def test_suma_digitos():
    assert suma_digitos(123456789) == 45
    assert suma_digitos(1234567890) == 45
    assert suma_digitos(0) == 0

def test_contar_digitos():
    assert contar_digitos(123456, 4) == 1
    assert contar_digitos(1223334444, 2) == 2

def test_factorial(): 
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(5) == 120

if __name__ == "__main__":
    pytest.main()