"""
Agenda de Citas - Lista Ligada
Seminario de Solución de Problemas de Algoritmia
Created By: Isaac Eduardo Sánchez Campos
Código: 211172172
"""

import os

class node:
    def __init__(self, day, month, desc):
        self.day = day
        self.month = month
        self.desc = desc
        self.next = None

    def __str__(self):
        string = "Dia: " + str(self.day) + "Mes: " + \
            str(self.month) + " desc: " + str(self.desc)
        return str(string)

class linked_list:
    def __init__(self):
        self.first = None
        self.size = 0

    def add(self):
        print("Ingresa el dia: ")
        day = self.read_int()
        print("Ingresa el mes:")
        month = self.read_int()
        desc = input("Ingresa la descripcion: ")
        os.system("clear")
        try:

            if self.validate_date(day, month):
                MyNode = node(day, month, desc)
                if self.size == 0:
                    self.first = MyNode
                else:
                    actual = self.first
                    while actual.next != None:
                        actual = actual.next
                    actual.next = MyNode

                self.size += 1
                print("Fecha agregada correctamente."+ str("\n"))
                return MyNode
        except:
            print("Fecha invalida, por favor agrega nuevamente."+ str("\n"))
            input()
            pass

    def read_int(self):
        """
        Solicita un valor entero y lo devuelve.
        Mientras el valor Ingresado no sea entero, vuelve a solicitarlo.
        """
        while True:
            valor = input()
            try:
                valor = int(valor)
                return valor
            except ValueError:
                print ("Alerta: Se debe ingresar un numero entero.")

    def validate_date(self, day, month):
        # Array que almacenara los dias que tiene cada mes)
        dias_mes = [31, 28, 31, 30,31, 30, 31, 31, 30, 31, 30, 31]

        # Comprobar que el mes sea valido
        if(month < 1 or month > 12):
            print("Fecha invalida, por favor agrega nuevamente.")
            input()
            return False

        # Comprobar que el dia sea valido
        month -= 1
        if(day <= 0 or day > dias_mes[month]):
            print("Fecha invalida, por favor agrega nuevamente.")
            input()
            return False

        # Si ha pasado todas estas condiciones, la fecha es válida
        return True

    def delete(self, day, month):
        if self.first.day == day and self.first.month == month:
            # Se descarta la cabecera de la lista
            input()
            deletedNode = self.first
            self.first = self.first.next
        else:
            actual = self.first
            try:
                while actual.next.day != day and actual.next.month != month:
                    if actual.next == None:
                        return False
                    else:
                        actual = actual.next
                deletedNode = actual.next
                actual.next = deletedNode.next
            except AttributeError:
                print("Dato no encontrado.")
                return False
        print("Dato eliminado.")
        self.size -= 1

        return deletedNode

    def get_day(self):
        return self.day

    def search(self):
        if self.size == 0:
            print("La agenda se encuentra vacia.")
            return False
        else:
            print ("Buscar"+ str("\n"))
            print("Ingresa el dia a buscar:")
            day = diary_list.read_int()
            print("Ingresa el mes a buscar:")
            month = diary_list.read_int()
            actual = self.first
            encontrado = False
            while actual != None and not encontrado:
                if actual.day == day and actual.month == month:
                    print(actual)
                    encontrado = True
                else:
                    actual = actual.next
            return encontrado

    def show(self):
        if self.size == 0:
            print("La agenda se encuentra vacia." + str("\n"))
        else:
            print(diary_list)
            print(str("\n"))

    def __len__(self):
        return self.size

    def __str__(self):
        # Se le da un formato a la fecha legible para el usuario
        string = ""
        actual = self.first
        month_name = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
        for i in range(len(self)):
            string += str(str(actual.day) + " de " + month_name[actual.month-1] + ": " + actual.desc)
            if i != len(self)-1:
                string += str("\n")
            actual = actual.next
        return string

diary_list = linked_list()
option = 0

while option != '5':
    # Menu principal
    os.system("clear")
    print("Agenda SA 2020" + str("\n"))
    print("1. Agregar")
    print("2. Borrar")
    print("3. Mostrar")
    print("4. Buscar")
    print("5. Salir")
    option = (input("Ingresa una opcion: "))

    if option == '1':
        # Invoca función de añadir
        os.system("clear")
        print ("Agregar"+ str("\n"))
        diary_list.add()
        input("Presiona Enter para continuar.")

    elif option == '2':
        # Invoca función de buscar
        os.system("clear")
        if diary_list.size != 0:
            print ("Borrar"+ str("\n"))
            print ("Buscar"+ str("\n"))
            print("Ingresa el Dia a borrar:")
            day = diary_list.read_int()
            print("Ingresa el Mes a borrar:")
            month = diary_list.read_int()
            diary_list.delete(day, month)
            input("Presiona Enter para continuar.")
        else:
            print("Lista vacia.")
            input("Presiona Enter para continuar.")

    elif option == '3':
        # Invoca función de mostrar
        os.system("clear")
        print ("Mostrar"+ str("\n"))
        diary_list.show()
        input("Presiona Enter para continuar.")

    elif option == '4':
        # Invoca función de buscar
        os.system("clear")
        if(diary_list.search() != True):
            print("No encontrado")
        input("Presiona Enter para continuar.")

    elif option == '5':
        # Invoca función para salir del programa
        os.system("clear")
        print ("Presiona Enter para salir.")
        input()

    else:
        # Alerta de opción inválida
        os.system("clear")
        print ("Por favor, ingresa una opcion valida.")
        input()
