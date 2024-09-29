import sys
sys.path.append('src')
from PriorityQueue.doubleLinkedList import DoubleLinkedList
from PriorityQueue.patient import Patient

class Queue:

    def __init__(self) -> None:
        self.linkedlist: DoubleLinkedList = DoubleLinkedList()
        self.id = 0

    def insertar(self, name, query_description, prioridad):
        self.id += 1
        patient = Patient(self.id, name, query_description, prioridad)
        self.linkedlist.append_patient(patient)

    def antender(self):
        patient_treated = self.linkedlist.head
        self.linkedlist.delete_position(0)
        return patient_treated
    
    def mostrar(self):
        print(f"{self.linkedlist}")
            
    def __repr__(self) -> str:
        return f"{self.linkedlist}"

obj = Queue()
