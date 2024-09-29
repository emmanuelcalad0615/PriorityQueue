class Patient:

    def __init__(self, id: int, name: str, query_description: str, priority:int = None) -> None:
        self.id: int = id
        self.name: str = name    
        self.query_description: str = query_description
        if priority == None:
            self.priority: int = self.priority_calculate(query_description)
        else:
            self.priority: int = priority     

    def quitar_tildes(self, text: str):
        accents = {
            "á": "a",
            "é": "e",
            "í": "i",
            "ó": "o",
            "ú": "u"    
        } 
        text = text.lower() 
        return "".join(accents.get(c, c) for c in text)  

    def priority_calculate(self, description: str):

        high_priority = ["dolor agudo", "fractura", "ataque", "hemorragia", "desmayo", "dificultad para respirar", "dolor en el pecho", "infarto"]
        medium_high_priority = ["fiebre alta", "crisis", "shock", "infección grave", "sangrado", "dolor intenso", "pérdida de consciencia"]
        medium_priority = ["fiebre", "tos", "náuseas", "vómitos", "dolor de cabeza", "cansancio", "dolor de estómago", "infección"]
        medium_low_priority = ["revisión", "control", "chequeo", "seguimiento", "consulta rutinaria", "vacunación", "prevención"]
        low_priority = ["consulta general", "pregunta", "información", "duda", "evaluación", "orientación"]

        description = self.quitar_tildes(description)

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