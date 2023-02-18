from random import choice


# Exercise 1 : Pets
print('\nExercise 1 : Cats\n=================')
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

cat01 = Bengal('Albert', 5)
cat02 = Bengal('Bernie', 10)
cat03 = Chartreux('Carlita', 6)
cat04 = Siamese('Dorothy', 17)
cat05 = Siamese('Emilio', 2)
my_cats = [cat01, cat02, cat03, cat04, cat05]
my_pets = Pets(my_cats)
my_pets.walk()


# Exercise 2 : Dogs
print('\nExercise 2 : Dogs\n=================')
class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    def bark(self):
        print(f"{self.name} is barking")
    def run_speed(self):
        return self.weight / self.age * 10
    def fight(self, other_dog):
        if self.run_speed() > other_dog.run_speed():
            print(f"{self.name} wins !")
        elif self.run_speed() < other_dog.run_speed():
            print(f"{other_dog.name} wins !")
        else:
            print("It's a tie !")
dog01 = Dog('Arnie', 8, 30)
dog02 = Dog('Bear', 9, 45)
dog03 = Dog('Cooper', 5, 30)
dog01.bark()
dog02.bark()
dog03.bark()
dog01.run_speed()
dog02.run_speed()
dog03.run_speed()
dog01.fight(dog01)
dog01.fight(dog02)
dog02.fight(dog03)



# Exercise 3 : Dogs Domesticated
class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained = trained
    def train(self):
        self.bark()
        self.trained = True
    def play(self, *args):
        list_dogs = [self.name]
        for indiv in args:
            list_dogs.append(indiv.name)
        print('\n' + ', '.join(list_dogs) + ' all play together\n')
    def do_a_trick(self):
        trick_list = [" does a barrel roll", " stands on back legs" , " gives paw", " plays dead"]
        if self.trained:
            print(f"\n{self.name}{choice(trick_list)}\n")

print("\nExercise 3 : Dogs Domesticated\n==============================")
dog10 = PetDog('Alfred', 4, 24, True)
dog11 = PetDog('Brady', 6, 8)
dog12 = PetDog('Carmen', 11, 19)
dog10.play(dog11, dog12)
dog10.play()
dog11.train()
dog11.do_a_trick()