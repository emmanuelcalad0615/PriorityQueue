class Patient:

    def __init__(self, id: int, name: str, query_description: str) -> None:
        if not name or not isinstance(name, str):
            raise ValueError("El nombre debe ser un valor de tipo str diferente de vacío")
        if not query_description or not isinstance(query_description, str):
            raise ValueError("La descripción debe ser un valor de tipo str diferente de vacío")
        self.id: int = id
        self.name: str = name    
        self.query_description: str = query_description
        self.priority: int = self.priority_calculate(query_description)
         

    def remove_accent(self, text: str) -> str:
        accents = {
            "á": "a",
            "é": "e",
            "í": "i",
            "ó": "o",
            "ú": "u"    
        } 
        text = text.lower() 
        return "".join(accents.get(c, c) for c in text)  

    def priority_calculate(self, description: str) -> int:
        priority_map = {
            "dolor agudo": 1,
            "fractura": 1,
            "ataque": 1,
            "hemorragia": 1,
            "desmayo": 1,
            "dificultad para respirar": 1,
            "dolor en el pecho": 1,
            "infarto": 1,
            "fiebre alta": 2,
            "crisis": 2,
            "shock": 2,
            "infeccion grave": 2,
            "sangrado": 2,
            "dolor intenso": 2,
            "pérdida de consciencia": 2,
            "fiebre": 3,
            "tos": 3,
            "nauseas": 3,
            "vomitos": 3,
            "dolor de cabeza": 3,
            "cansancio": 3,
            "dolor de estomago": 3,
            "infeccion": 3,
            "revision": 4,
            "control": 4,
            "chequeo": 4,
            "seguimiento": 4,
            "consulta rutinaria": 4,
            "vacunacion": 4,
            "prevencion": 4,
            "consulta general": 5,
            "pregunta": 5,
            "informacion": 5,
            "duda": 5,
            "evaluacion": 5,
            "orientacion": 5
        }

        description = self.remove_accent(description)

        for key, priority in priority_map.items():
            if key in description:
                return priority

        return 6

    def __repr__(self) -> str:
        return f"({self.id} - {self.name} - {self.query_description} - {self.priority})"

 

"""patients = {
    "Juan Perez": "sufre de dolor agudo en el abdomen",  #  1
    "Maria Lopez": "necesita una consulta rutinaria para chequeo",  #  4
    "Carlos Gomez": "presenta una fractura en el brazo",  #  1
    "Ana Torres": "tiene tos persistente y necesita evaluación",  # 3
    "Luis Fernandez": "experimenta dolor intenso en la espalda",  #  2
    "Elena Martinez": "reporta fiebre alta desde hace tres días",  # 2
    "Pedro Alvarez": "sufre de infección grave en el pie",  #  2
    "Sofia Reyes": "asiste a una consulta general anual",  #  5
    "Luis Gomez": "tiene preguntas sobre su tratamiento actual",  #  5
    "Carlos Ruiz": "presenta dificultad para respirar después de hacer ejercicio"  #  1
}


for name, description in patients.items():
    i = 0
    patient = Patient(i, name, description)  
    print(f"Paciente: {patient.name}, Descripción: '{patient.query_description}', Prioridad: {patient.priority}")
    i += 1"""
