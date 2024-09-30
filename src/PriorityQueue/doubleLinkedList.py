
import sys
sys.path.append("src")
from PriorityQueue.patient import Patient
class EmptyDoubleLinkedList(Exception):
    pass

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
            while nodo.next != None:
                if nodo.value.priority > nodo_add.value.priority: 
                    break
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

            elif nodo.prev == None:
                head_ant = self.head
                self.head = nodo_add
                self.head.next = head_ant
                head_ant.prev = self.head
                
            elif nodo.next == None and nodo.value.priority <= nodo_add.value.priority:
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
    
    def delete_id(self, id: int):
        if self.size == 0: 
            raise EmptyDoubleLinkedList("Lista vacía")
        if self.size == 1:
            if self.head.value.id == id:
                self.head = None
                self.tail = None
                self.size -= 1
            else:
                return "ID no encontrado"        
        else:
            nodo = self.head
            while nodo.next != None:
                if nodo.value.id == id:
                    break
                nodo = nodo.next

            if nodo.prev == None:
                self.head = nodo.next
                self.head.prev = None
                nodo.next = None
                self.size -= 1

            elif nodo.next == None:
                if nodo.value.id == id:
                    self.tail = nodo.prev
                    self.tail.next = None
                    nodo.prev = None
                    self.size -= 1
                else:
                    return "ID no encontrado"    

            else:
                previous_nodo = nodo.prev
                next_nodo = nodo.next
                nodo.prev = None
                nodo.next = None
                previous_nodo.next = next_nodo
                next_nodo.prev = previous_nodo
                self.size -= 1
                
    def delete_position(self, position: int):
        if self.size == 0: 
            raise EmptyDoubleLinkedList("Lista vacía")
        
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
            previous_nodo = nodo.prev
            next_nodo = nodo.next
            nodo.prev = None
            nodo.next = None
            next_nodo.prev = previous_nodo
            previous_nodo.next = next_nodo
            self.size -= 1             
    
    def __repr__(self):
        return str(self.head)    