#--------------------Ejercicio 2--------------------

class Cuenta:
    #Constructor de la clase
    def _init_(self, owner, amount):
        self.owner= owner
        self.amount= amount

    #Getter del titular
    def get_owner(self):
        return self.owner

    #Setter del titular, con el adicional de tener que retirar o ingresar dinero para efectuar la modivicación
    def set_owner(self, owner):
        print("Para cambiar el titular necesita ingresar o retirar dinero.")
        print("Seleccione el movimiento que desee hacer: `1´= Ingresar dinero; `2´= Retirar dinero; `3´= Cancelar operación")
        exit= False
        while (exit == False):
            choice= input()
            if (choice.isdigit()):
                choice= int(choice)
                if (choice == 1):
                    amount_in= int(input("Ingrese la cantidad de dinero que desea ingresar: "))
                    self.deposit(amount_in)
                    self.owner= owner
                    exit= True
                elif (choice == 2):
                    amount_out= int(input("Ingrese la cantidad de dinero que desea retirar: "))
                    self.withdraw(amount_out)
                    self.owner= owner
                    exit= True
                elif (choice == 3):
                    exit= True
                else:
                    print("Por favor, ingrese una de las opciones proporcionadas: 1, 2 o 3")
            else:
                print("Por favor, ingrese una de las opciones proporcionadas: 1, 2 o 3")

    #Getter de la cantidad
    def get_amount(self):
        return self.amount

    #Setter de la cantidad, con el adicional de tener que retirar o ingresar dinero para efectuar la modivicación
    def set_amount(self, amount):
        print("Para cambiar el monto de su cuenta necesita ingresar o retirar dinero.")
        print("Seleccione el movimiento que desee hacer: `1´= Ingresar dinero; `2´= Retirar dinero; `3´= Cancelar operación")
        exit= False
        while (exit == False):
            choice= input()
            if (choice.isdigit()):
                choice= int(choice)
                if (choice == 1):
                    self.amount= amount
                    exit= True
                elif (choice == 2):
                    amount_out= int(input("Ingrese la cantidad de dinero que desea retirar: "))
                    self.withdraw(amount_out)
                    self.amount= amount
                    exit= True
                elif (choice == 3):
                    exit= True
                else:
                    print("Por favor, ingrese una de las opciones proporcionadas: 1, 2 o 3")
            else:
                print("Por favor, ingrese una de las opciones proporcionadas: 1, 2 o 3")

    #Método para mostrar los datos de la cuenta
    def show(self):
        print(f"Títular: {self.owner}")
        print(f"Saldo: {self.amount: .2f}$")

    #Método para ingresar dinero
    def deposit(self, amount):
        if (amount > 0):
            self.amount+= amount

    #Método para retirar dinero
    def withdraw(self, amount):
        self.amount-= amount


#Programa principal

cuenta1= Cuenta("Mariano Gonzales", 5000.00)
print(cuenta1.get_owner())
print(cuenta1.get_amount())
cuenta1.set_owner("María Lopez")
cuenta1.set_amount(7500.00)
cuenta1.show()
cuenta1.deposit(1500.50)
cuenta1.withdraw(4000.00)

