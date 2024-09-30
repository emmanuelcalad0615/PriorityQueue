class Patient:

    def __init__(self, id: int, name: str, query_description: str, priority:int = None) -> None:
        self.id: int = id
        self.name: str = name    
        self.query_description: str = query_description
        if priority == None:
            self.priority: int = self.priority_calculate(query_description)
        else:
            self.priority: int = priority     

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

        high_priority = ["dolor agudo", "fractura", "ataque", "hemorragia", "desmayo", "dificultad para respirar", "dolor en el pecho", "infarto"]
        medium_high_priority = ["fiebre alta", "crisis", "shock", "infeccion grave", "sangrado", "dolor intenso", "pérdida de consciencia"]
        medium_priority = ["fiebre", "tos", "nauseas", "vomitos", "dolor de cabeza", "cansancio", "dolor de estomago", "infeccion"]
        medium_low_priority = ["revision", "control", "chequeo", "seguimiento", "consulta rutinaria", "vacunacion", "prevencion"]
        low_priority = ["consulta general", "pregunta", "informacion", "duda", "evaluacion", "orientacion"]

        description = self.remove_accent(description)

        for word in high_priority:
            if word in description:
                return 1
            
        for word in medium_high_priority:
            if word in description:
                return 2
            
        for word in medium_priority:
            if word in description:
                return 3
            
        for word in medium_low_priority:
            if word in description:
                return 4
            
        for word in low_priority:
            if word in description:
                return 5

    def __repr__(self) -> str:
        return f"({self.id} - {self.name} - {self.query_description} - {self.priority})"

 
