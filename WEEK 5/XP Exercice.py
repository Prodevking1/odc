# Exercise 3: Who's The Song Producer?
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


stairway = Song(["There’s a lady who's sure", "all that glitters is gold",
                "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()


# Exercise 4: Afternoon At The Zoo
class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print("The animals in the zoo are:")
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been sold.")
        else:
            print(f"{animal_sold} is not in the zoo.")

    def sort_animals(self):
        sorted_animals = {}
        for animal in self.animals:
            if animal[0] not in sorted_animals:
                sorted_animals[animal[0]] = [animal]
            else:
                sorted_animals[animal[0]].append(animal)

        print("The animals in the zoo are sorted alphabetically and grouped by their first letter:")
        for key, value in sorted(sorted_animals.items()):
            print(f"{key}: {value}")

    def get_groups(self):
        print("The animals in the zoo grouped by their first letter are:")
        sorted_animals = {}
        for animal in self.animals:
            if animal[0] not in sorted_animals:
                sorted_animals[animal[0]] = [animal]
            else:
                sorted_animals[animal[0]].append(animal)

        for key, value in sorted(sorted_animals.items()):
            animals = ", ".join(value)
            if len(value) > 1:
                print(f"{key}: [{animals}]")
            else:
                print(f"{key}: {animals}")


ramat_gan_safari = Zoo("Ramat Gan Safari")
ramat_gan_safari.add_animal("Ape")
ramat_gan_safari.add_animal("Bear")
ramat_gan_safari.add_animal("Baboon")
ramat_gan_safari.add_animal("Cat")
ramat_gan_safari.add_animal("Cougar")
ramat_gan_safari.add_animal("Emu")
ramat_gan_safari.add_animal("Eel")
ramat_gan_safari.get_animals()
ramat_gan_safari.sell_animal("Ape")
ramat_gan_safari.get_animals()
ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups()
