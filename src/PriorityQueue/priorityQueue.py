import sys
sys.path.append('src')
from PriorityQueue.doubleLinkedList import DoubleLinkedList
from PriorityQueue.patient import Patient
from PriorityQueue.doubleLinkedList import Node


class PriorityQueue:

    def __init__(self) -> None:
        self.linkedlist: DoubleLinkedList = DoubleLinkedList()
        self.id = 0

    def insertar(self, name: str, query_description: str):
        self.id += 1
        patient = Patient(self.id, name, query_description)
        self.linkedlist.append_patient(patient)

    def antender(self) -> Node:
        patient_treated = self.linkedlist.head
        self.linkedlist.delete_position(0)
        return patient_treated
    
    def cancelar(self, id: int):
        self.linkedlist.delete_id(id)

    
    def mostrar(self):
        print(f"{self.linkedlist}")
            
    def __repr__(self) -> str:
        return f"{self.linkedlist}"

obj = PriorityQueue()

"""obj.insertar("Paciente A", "dolor agudo", 4)
obj.insertar("Paciente B", "Consulta 2", 1)
obj.insertar("Paciente C", "Consulta 3", 5)
print(obj)  # Debería ser: Paciente B, Paciente A, Paciente C"""

"""obj.insertar("Paciente A", "Consulta", 3)
obj.insertar("Paciente B", "Consulta", 5)
obj.insertar("Paciente C", "Consulta", 1)
obj.insertar("Paciente D", "Consulta", 4)
obj.mostrar()  # Debe ser: Paciente C, Paciente A, Paciente D, Paciente B
print(type(obj.antender()))
obj.mostrar()"""

"""obj.insertar("Paciente 1", "Consulta", 2)
obj.insertar("Paciente 2", "Consulta", 2)
obj.insertar("Paciente 3", "Consulta", 2)
print(obj)  # Debería ser: Paciente 1, Paciente 2, Paciente 3"""

"""obj.insertar("Paciente 1", "Consulta", 1)
obj.insertar("Paciente 2", "Consulta", 2)
obj.insertar("Paciente 3", "Consulta", 3)
print(obj)  # Debería ser: Paciente 1, Paciente 2, Paciente 3"""

"""obj.insertar("Paciente 1", "Consulta", 4)
obj.insertar("Paciente 2", "Consulta", 1)
obj.insertar("Paciente 3", "Consulta", 5)
print(obj)  # Debe ser: Paciente 2, Paciente 1, Paciente 3 

obj.cancelar(3)
print(obj)"""
