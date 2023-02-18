class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = {}
    
    def add_animal(self, animal, quantity=1):
        if animal in self.animals:
            self.animals[animal] += quantity
        else:
            self.animals[animal] = quantity
    
    def get_info(self):
        info = f"{self.name}'s farm\n\n"
        for animal, quantity in sorted(self.animals.items()):
            info += f"{animal} : {quantity}\n"
        return info + "\tE-I-E-I-0!"
    
    def get_animal_types(self):
        return sorted(list(self.animals.keys()))
    
    def get_short_info(self):
        animal_types = ", ".join(self.get_animal_types())
        return f"{self.name}'s farm has {animal_types}."

macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())

animal_types = macdonald.get_animal_types()
print(animal_types)

short_info = macdonald.get_short_info()
print(short_info)
