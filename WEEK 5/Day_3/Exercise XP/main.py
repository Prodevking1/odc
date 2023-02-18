# Exercise 1 : Built-in functions
print('\nExercise 1 : \n=================')
def use_built_in():
    """
    1. Function abs() return the abolute value of a number (integer or float)
    2. Function int() uses two parameters : value and base
    3. Function raw-input() is not used in Python 3
    """
    sample_list = [ 1, -1, 2/3, -4/3]
    for el in sample_list:
        print(f"abs({el}) -> {abs(el)}")
        print(f"int({el}) -> {int(el)}")
    print(int('1011010111', 2))

use_built_in()

# Exercise 2 : Currencies
print('\nExercise 2 : \n=================')
class Currency():
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def __str__(self):
        plurals = 's'
        if self.amount <= 1:
            plurals = ''
        return f"'{self.amount} {self.name}{plurals}'"

    def __repr__(self):
        plurals = 's'
        if self.amount <= 1:
            plurals = ''
        return f"'{self.amount} {self.name}{plurals}'"

    def __int__(self):
        return int(self.amount)

    def __add__(self, other):
        if isinstance(other, Currency):
            if self.name != other.name:
                raise TypeError(f"Cannot add between Currency type <{self.name}> and <{other.name}>")
        return int(self) + int(other)

    def __iadd__(self, other):
        if isinstance(other, Currency):
            if self.name != other.name:
                raise TypeError(f"Cannot add between Currency type <{self.name}> and <{other.name}>")
        self.amount = int(self) + int(other)

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c4 = Currency('shekel', 1)
c3 = Currency('shekel', 10)

print(str(c1))
print(repr(c1))
print(int(c1))
print(c1 + 5)
print(c1 + c2)
try:
    print(c1 + c3)
except TypeError as e:
    print('TypeError:', e)