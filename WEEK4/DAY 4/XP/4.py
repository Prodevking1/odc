import random

def randomNumber(z):
    Numb = random.randint(1, 100)
    if z == Numb:
        print(f"Success!!!\nNumber {z} and the random number {Numb}")
    else:
        print(f"Failure... The user number is {z} and the random number is {Numb}")
    randomNumber(99)

randomNumber(99)
