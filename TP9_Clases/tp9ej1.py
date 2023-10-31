class Persona:
    def _init_(self, name="", age=0, dni=""):
        self.name = name
        self.age = age
        self.dni = dni

    def get_name(self):
        return self.name

    def set_name(self, name):
        if isinstance(name, str):
            self.name = name
        else:
            print("Error: El nombre debe ser una cadena de caracteres.")

    def get_age(self):
        return self.age

    def set_age(self, age):
        if isinstance(age, int) and age >= 0:
            self.age = age
        else:
            print("Error: La edad debe ser un número entero no negativo.")

    def get_dni(self):
        return self.dni

    def set_dni(self, dni):
        if isinstance(dni, str):
            self.dni = dni
        else:
            print("Error: El DNI debe ser una cadena de caracteres.")

    def mostrar(self):
        print(f"Nombre: {self.name}")
        print(f"Edad: {self.age}")
        print(f"DNI: {self.dni}")

    def legalage(self):
        if self.age >= 18:
            print("Es mayor de edad")
        else:
            print("No es mayor de edad")



#Ejercicio 1 - main

persona1 = Persona("Lucas", 16, "44349212")
persona1.mostrar()
persona1.legalage()