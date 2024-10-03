import sys
sys.path.append('src')
from PriorityQueue.doubleLinkedList import DoubleLinkedList, IDError, EmptyDoubleLinkedList, DimensionError
from PriorityQueue.patient import Patient
from PriorityQueue.doubleLinkedList import Node

class PriorityQueue:
    def __init__(self) -> None:
        self.linkedlist = DoubleLinkedList()
        self.id = 0

    def insertar(self, name: str, query_description: str):

        try:
            self.id += 1
            patient = Patient(self.id, name, query_description)
            self.linkedlist.append_patient(patient)
            print(f"Paciente {patient.name} insertado con prioridad {patient.priority}.")

        except ValueError as e:
            print(f"Error al insertar paciente: {e}")

        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

    def antender(self):

        try:
            if self.linkedlist.size == 0:
                raise EmptyDoubleLinkedList("No hay pacientes en la cola.")
            patient_treated = self.linkedlist.head
            self.linkedlist.delete_position(0)
            print(f"Paciente atendido: {patient_treated.value.name}.")

        except EmptyDoubleLinkedList as e:
            print(f"Error: {e}")

        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

    def cancelar(self, id: int):
        try:
            self.linkedlist.delete_id(id)
            print(f"Paciente con ID {id} cancelado.")

        except IDError as e:
            print(f"Error: {e}")

        except EmptyDoubleLinkedList as e:
            print(f"Error: {e}")

        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

    def mostrar(self):
        print(f"Estado actual de la cola: {self.linkedlist}")

"""priority_queue = PriorityQueue()

patients = {
    "Juan Perez": "sufre de dolor agudo en el abdomen",
    "Maria Lopez": "necesita una consulta rutinaria para chequeo",
    "Carlos Gomez": "presenta una fractura en el brazo",
    "Ana Torres": "tiene tos persistente y necesita evaluación",
    "Luis Fernandez": "experimenta dolor intenso en la espalda",
    "Elena Martinez": "reporta fiebre alta desde hace tres días",
    "Pedro Alvarez": "sufre de infección grave en el pie",
    "Sofia Reyes": "asiste a una consulta general anual",
    "Luis Gomez": "tiene preguntas sobre su tratamiento actual",
    "Carlos Ruiz": "presenta dificultad para respirar después de hacer ejercicio"
}

for name, description in patients.items():
    priority_queue.insertar(name, description)

priority_queue.antender()

priority_queue.cancelar(2)

priority_queue.mostrar()"""

