
"""
Agenda de Citas
Seminario de Algoritmia
CreatedBy: ZackSanchez
"""
import os 
import msvcrt


class nodo:
    def __init__(self, dia, mes, desc):
        self.dia = dia
        self.mes = mes
        self.desc = desc
        self.next = None

    def __str__(self):
        string = "dia: " + str(self.dia) + "mes: " + \
            str(self.mes) + " desc: " + str(self.desc)
        return str(string)


class LinkedList:
    def __init__(self):
        self.First = None
        self.Size = 0

    def Agregar(self):


        print("ingresa el dia")
        dia = self.lee_entero()
        print("ingresa el mes")
        mes = self.lee_entero()
        desc = input("Ingresa la descripcion: ")
        os.system("clear")
        try:

            if self.ValidarFecha(dia, mes):
                MyNode = nodo(dia, mes, desc)
                if self.Size == 0:
                    self.First = MyNode
                else:
                    actual = self.First
                    while actual.next != None:
                        actual = actual.next
                    actual.next = MyNode

                self.Size += 1
                print("Fecha agregada correctamente"+ str("\n"))
                return MyNode
        except:
            print("Fecha invalida, agrega nuevamente"+ str("\n"))
            input()
            pass

    def lee_entero(self):
        """ Solicita un valor entero y lo devuelve.
            Mientras el valor ingresado no sea entero, vuelve a solicitarlo. """
        while True:
            valor = input()
            try:
                valor = int(valor)
                return valor
            except ValueError:
                print ("Atencion: Debe ingresar un numero entero.")

    def ValidarFecha(self, dia, mes):
        #Array que almacenara los dias que tiene cada mes)
        dias_mes = [31, 28, 31, 30,31, 30, 31, 31, 30, 31, 30, 31]
 
        #Comprobar que el mes sea valido
        if(mes < 1 or mes > 12):
            print("Fecha invalida, agrega nuevamente")
            input()
            return False
         
        #Comesprobar que el dia sea valido
        mes -= 1
        if(dia <= 0 or dia > dias_mes[mes]):
            print("Fecha invalida")
            input()
            return False
     
        #Si ha pasado todas estas condiciones, la fecha es valida
        return True

    def Borrar(self, dia, mes):
        if self.First.dia == dia and self.First.mes == mes:
            # Se descarta la cabecera de la lista
            input()
            deletedNode=self.First
            self.First = self.First.next
        else:
            actual = self.First
            try:
                while actual.next.dia != dia and actual.next.mes != mes:
                    if actual.next == None:
                        return False
                    else:
                        actual = actual.next
                deletedNode = actual.next
                actual.next = deletedNode.next
            except AttributeError:
                print("Elemento no encontrado")
                return False
        print("Elemento eliminado")
        self.Size -= 1

        return deletedNode

    def obtenerDia(self):
        return self.dia

    def Buscar(self):
        if self.Size == 0:
            print("La lista esta vacia.")
            return False
        else:
            print ("Buscar"+ str("\n"))
            print("ingresa el dia a buscar")
            dia = MyList.lee_entero()
            print("ingresa el mes a buscar")
            mes = MyList.lee_entero()
            actual = self.First
            encontrado = False
            while actual != None and not encontrado:
                if actual.dia == dia and actual.mes == mes:
                    print(actual)
                    encontrado = True
                else:
                    actual = actual.next
            return encontrado

    def Mostrar(self):
        if self.Size ==0:
            print("Lista Vacia" + str("\n"))
        else:
            print(MyList)
            print(str("\n"))

    def __len__(self):
        return self.Size

    def __str__(self):
        string = " "
        actual = self.First
        nombre_mes = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
        for i in range(len(self)):
            string += str(str(actual.dia) + " de " + nombre_mes[actual.mes-1] + ": " + actual.desc)
            if i != len(self)-1:
                string += str("\n")
            actual = actual.next
        return string


MyList = LinkedList()
opcion = 0

while opcion != '5':
    os.system("clear") 
    print("Agenda SA 2020" + str("\n"))
    print("1. Agregar")
    print("2. Borrar")
    print("3. Mostrar")
    print("4. Buscar")
    print("5. Salir")
    opcion = (input("Ingrese su opcion: "))

    if opcion == '1':
        os.system("clear") 
        print ("Agregar"+ str("\n"))
        MyList.Agregar()
        input("Presione Enter para continuar")

    elif opcion == '2':
        os.system("clear")
        if MyList.Size != 0: 
            print ("Borrar"+ str("\n"))
            print ("Buscar"+ str("\n"))
            print("ingresa el dia a borrar")
            dia = MyList.lee_entero()
            print("ingresa el mes a borrar")
            mes = MyList.lee_entero()
            MyList.Borrar(dia, mes)
            input("Presione Enter para continuar")
        else:
            print("Lista vacia.")
            input("Presione Enter para continuar")

    elif opcion == '3':
        os.system("clear") 
        print ("Mostrar"+ str("\n"))
        MyList.Mostrar()
        input("Presione Enter para continuar")

    elif opcion == '4':
        os.system("clear") 
        if(MyList.Buscar() != True):
            print("No encontrado")
        input("Presione Enter para continuar")

    elif opcion == '5':
        os.system("clear") 
        print ("presione Enter para salir")
        input()

    else:
        os.system("clear") 
        print ("ingrese una opcion valida")
        input()


