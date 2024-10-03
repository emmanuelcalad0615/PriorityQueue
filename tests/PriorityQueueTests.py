import unittest
import sys 
sys.path.append("src")
from PriorityQueue.patient import Patient
from PriorityQueue.doubleLinkedList import DoubleLinkedList, IDError, EmptyDoubleLinkedList
from PriorityQueue.priorityQueue import PriorityQueue

class TestPatient(unittest.TestCase):

    def test_patient_creation(self):
        patient = Patient(1, "Juan Perez", "sufre de dolor agudo en el abdomen")
        self.assertEqual(patient.name, "Juan Perez")
        self.assertEqual(patient.query_description, "sufre de dolor agudo en el abdomen")
        self.assertEqual(patient.priority, 1)  

    def test_patient_invalid_name(self):
        with self.assertRaises(ValueError) as context:
            Patient(1, "", "sufre de dolor agudo en el abdomen")
        self.assertEqual(str(context.exception), "El nombre debe ser un valor de tipo str diferente de vacío")

    def test_patient_invalid_description(self):
        with self.assertRaises(ValueError) as context:
            Patient(1, "Juan Perez", "")
        self.assertEqual(str(context.exception), "La descripción debe ser un valor de tipo str diferente de vacío")

class TestDoubleLinkedList(unittest.TestCase):

    def setUp(self):
        self.linkedlist = DoubleLinkedList()

    def test_append_patient(self):
        patient = Patient(1, "Juan Perez", "sufre de dolor agudo en el abdomen")
        self.linkedlist.append_patient(patient)
        self.assertEqual(self.linkedlist.size, 1)
        self.assertEqual(self.linkedlist.head.value, patient)

    def test_delete_id(self):
        patient1 = Patient(1, "Juan Perez", "sufre de dolor agudo en el abdomen")
        patient2 = Patient(2, "Maria Lopez", "necesita una consulta rutinaria para chequeo")
        self.linkedlist.append_patient(patient1)
        self.linkedlist.append_patient(patient2)
        
        self.linkedlist.delete_id(1)
        self.assertEqual(self.linkedlist.size, 1)
        self.assertEqual(self.linkedlist.head.value, patient2)

    def test_delete_id_not_found(self):
        with self.assertRaises(IDError):
            self.linkedlist.delete_id(99) 

    def test_delete_from_empty_list(self):
        with self.assertRaises(EmptyDoubleLinkedList):
            self.linkedlist.delete_id(1)

class TestPriorityQueue(unittest.TestCase):

    def setUp(self):
        self.queue = PriorityQueue()
        self.patients_data = {
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

        for name, description in self.patients_data.items():
            self.queue.insertar(name, description)

    def test_insert_patient(self):
        self.assertEqual(self.queue.linkedlist.size, len(self.patients_data))

    def test_antender_patient(self):
        self.queue.antender()
        self.assertEqual(self.queue.linkedlist.size, len(self.patients_data) - 1)

    def test_cancel_patient(self):
        self.queue.cancelar(1)  
        self.assertEqual(self.queue.linkedlist.size, len(self.patients_data) - 1)

    def test_cancel_patient_not_found(self):
        with self.assertRaises(IDError):
            self.queue.cancelar(99)  

if __name__ == "__main__":
    unittest.main()