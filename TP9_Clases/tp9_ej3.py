class Triangle:
    #Constructor de la clase
    def _init_(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    #Método para mostrar cuál es el lado del triangulo más largo
    def longest_side(self):
        return max(self.side1, self.side2, self.side3)

    #Método para mostrar el tipo de triángulo de en base a la longitud de sus lados
    def triangle_type(self):
        if self.side1 == self.side2 == self.side3:
            return "Equilátero"
        elif self.side1 == self.side2 or self.side1 == self.side3 or self.side2 == self.side3:
            return "Isósceles"
        else:
            return "Escaleno"


#Programa principal

side1, side2, side3= 12, 30, 15

triangle1 = Triangle(side1, side2, side3)
print(f"El lado más largo del triángulo es {triangle1.longest_side()}")
print(f"El triángulo es de tipo {triangle1.triangle_type()}")