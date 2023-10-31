class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.name} - {self.phone} - {self.email}"

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        contact = Contact(name, phone, email)
        self.contacts.append(contact)

    def list_contacts(self):
        for contact in self.contacts:
            print(contact)

    def find_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

    def edit_contact(self, name):
        contact = self.find_contact(name)
        if contact:
            print("Deje el campo vacío si no desea modificar el valor.")
            new_name = input("Nuevo nombre: ")
            new_phone = input("Nuevo teléfono: ")
            new_email = input("Nuevo email: ")
            
            if new_name:
                contact.name = new_name
            if new_phone:
                contact.phone = new_phone
            if new_email:
                contact.email = new_email
        else:
            print("Contacto no encontrado.")

    def menu(self):
        while True:
            print("1. Añadir contacto")
            print("2. Lista de contactos")
            print("3. Buscar contacto")
            print("4. Editar contacto")
            print("5. Cerrar agenda")
            
            option = input("Elige una opción: ")
            
            if option == "1":
                name = input("Nombre: ")
                phone = input("Teléfono: ")
                email = input("Email: ")
                self.add_contact(name, phone, email)
            elif option == "2":
                self.list_contacts()
            elif option == "3":
                name = input("Nombre del contacto a buscar: ")
                contact = self.find_contact(name)
                if contact:
                    print(contact)
                else:
                    print("Contacto no encontrado.")
            elif option == "4":
                name = input("Nombre del contacto a editar: ")
                self.edit_contact(name)
            elif option == "5":
                print("Cerrando agenda...")
                break
            else:
                print("Opción inválida.")

if __name__ == "__main__":
    address_book = AddressBook()
    address_book.menu()
