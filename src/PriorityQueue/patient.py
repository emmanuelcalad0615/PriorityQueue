class Patient:

    def __init__(self, id: int, name: str, query_description: str) -> None:
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

 
