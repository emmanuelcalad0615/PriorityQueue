import sys
sys.path.append("src")
from PriorityQueue.priorityQueue import PriorityQueue

class InvalidInputError(Exception):
    pass

class MainController:
    def __init__(self):
        self.queue = PriorityQueue()

    def mostrar_menu(self):
        print("MENÚ")
        print("1. Insertar paciente")
        print("2. Atender paciente")
        print("3. Cancelar paciente")
        print("4. Mostrar pacientes en cola")
        print("5. Salir")

    def insertar_paciente(self):
        name = input("Ingresa el nombre del paciente: ")
        description = input("Ingresa la descripción de la consulta: ")
        if not name or not description:
            raise InvalidInputError("El nombre y la descripción no pueden estar vacíos.")
        insert = self.queue.insertar(name, description)
        if insert:
            print(f"Paciente '{name}' insertado en la cola.")

    def atender_paciente(self):
        if self.queue.linkedlist.size == 0:
            print("No hay pacientes en la cola para atender.")
        else:
            paciente_atendido = self.queue.antender()
            print(f"Se ha atendido a: {paciente_atendido.value.name}")

    def cancelar_paciente(self):
        patient_id = input("Ingresa el ID del paciente a cancelar: ")
        if not patient_id.isdigit():
            raise InvalidInputError("El ID debe ser un número.")
        cancel = self.queue.cancelar(int(patient_id))
        if cancel:
            print(f"Paciente con ID {patient_id} cancelado.")

    def mostrar_pacientes(self):
        if self.queue.linkedlist.size == 0:
            print("No hay pacientes en la cola.")
        else:
            print("Pacientes en cola:")
            nodo = self.queue.linkedlist.head
            while nodo is not None:
                print(f"ID: {nodo.value.id}, Nombre: {nodo.value.name}, Prioridad: {nodo.value.priority}")
                nodo = nodo.next

    def ejecute(self):
        while True:
            self.mostrar_menu()
            try:
                choice = input("Selecciona una opción: ")

                if choice == "1":
                    self.insertar_paciente()
                elif choice == "2":
                    self.atender_paciente()
                elif choice == "3":
                    self.cancelar_paciente()
                elif choice == "4":
                    self.mostrar_pacientes()
                elif choice == "5":
                    print("Saliendo del programa.")
                    break
                else:
                    raise InvalidInputError("Opción no válida, intenta de nuevo.")

            except InvalidInputError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Ocurrió un error inesperado: {e}")