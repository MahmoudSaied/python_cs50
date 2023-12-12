import random

class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Slytherin"]
    
    @classmethod
    def sort(cls, name):
        house = random.choice(cls.houses)
        print(f"{name} is from {house}")
    
Hat.sort("Memo")