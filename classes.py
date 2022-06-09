#santi no se queria meter en esto

class People:
    amount: int = 0
    
    def __init__(self,name: str):
        self.name = name
        People.add_person()

    @classmethod
    def get_amount_of_people(cls):
        return cls.amount
    
    @classmethod
    def add_person(cls):
        cls.amount += 1

    @staticmethod   # ponele usar que la clase Circle (aunque esta clase no es Circle) tenga un metodo estatico que devuelve el valor de pi
    def pi():
        return 3.14

pepito = People('pepe')
juansito = People('juan')


print(People.get_amount_of_people())

