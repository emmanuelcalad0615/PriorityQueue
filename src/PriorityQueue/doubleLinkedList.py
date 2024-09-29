import sys
sys.path.append("src")
from PriorityQueue.patient import Patient
class Node:

    def __init__(self, patient: Patient) -> None:
        self.value: Patient = patient 
        self.next: Node = None
        self.prev: Node = None

    def __repr__(self) -> str:
        return f"{self.value} -> {self.next}"

class DoubleLinkedList:

    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0
        
    def append_patient(self, patient: Patient):
        nodo_add = Node(patient)
        if self.size == 0: 
            self.head = nodo_add  
            self.tail = nodo_add     
        else:
            nodo = self.head
            count = 1
            while nodo.next != None:
                if nodo.value.priority > nodo_add.value.priority: 
                    break
                count +=1
                nodo = nodo.next 
            if self.size == 1: 
                if nodo.value.priority <= nodo_add.value.priority:   
                    self.tail = nodo_add
                    self.head.next = self.tail
                    self.tail.prev = self.head  
                else: 
                    head_ant = self.head
                    self.head = nodo_add
                    self.head.next = head_ant
                    head_ant.prev = self.head

            elif count == 1:
                head_ant = self.head
                self.head = nodo_add
                self.head.next = head_ant
                head_ant.prev = self.head
                
            elif count == self.size and count != 1 and nodo.value.priority <= nodo_add.value.priority:
                tail_ant = self.tail
                self.tail = nodo_add
                tail_ant.next = self.tail
                self.tail.prev = tail_ant
                
            else:
                nodo_ant = nodo.prev
                nodo_ant.next = nodo_add
                nodo_add.prev = nodo_ant
                nodo_add.next = nodo
                nodo.prev = nodo_add

        self.size += 1

    def delete_position(self, position: int):
        if self.size == 0:
            return "Lista vacía"
        
        if self.size - 1 < position or position < 0:
            return "Supera las dimensiones de la lista"
        
        if self.size == 1:
            self.tail = None
            self.head = None
            self.size -= 1 

        elif self.size != 0 and position == 0:
            nodo_del = self.head
            self.head = nodo_del.next
            nodo_del.next = None
            self.head.prev = None
            self.size -= 1  

        elif position == self.size - 1:
             tail_ant = self.tail
             self.tail = tail_ant.prev
             tail_ant.prev = None
             self.tail.next = None
             self.size -= 1     

        else:
            nodo = self.head
            for i in range(0, position):
                nodo = nodo.next
            nodo_anterior = nodo.prev
            nodo_siguiente = nodo.next
            nodo.prev = None
            nodo.next = None
            nodo_siguiente.prev = nodo_anterior
            nodo_anterior.next = nodo_siguiente
            self.size -= 1             
    
    def __repr__(self):
        return str(self.head)    