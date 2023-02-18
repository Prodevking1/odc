from math import pi

class Circle():
    def __init__(self,size, d_or_r):
        self.radius = size
        self.diameter = 2 * size
        if d_or_r in ['d', 'D']:
            self.radius = size / 2
            self.diameter = size

    def __repr__(self):
        out = f"Circle with radius = {self.radius}."
        return out
    
    def area(self):
        return pi * self.radius ** 2
    
    def __add__(self, other):
        if not isinstance(other, Circle):
            print(f"{other} is not a circle.")
            return
        new_c = Circle(self.radius + other.radius, 'r')
        return new_c

    def __gt__(self, other):
        if not isinstance(other, Circle):
            print(f"{other} is not a circle.")
            return
        if self.radius > other.radius:
            return True
        return False

    def __eq__(self, other):
        if not isinstance(other, Circle):
            print(f"{other} is not a circle.")
            return
        if self.radius == other.radius:
            return True
        return False

    @staticmethod
    def sort_list(list_circles):
        for i in range(len(list_circles)):
            if not isinstance(list_circles[i], Circle):
                print(f"{list_circles[i]} is not a circle.")
                return
            for j in range(i+1, len(list_circles)):
                if not isinstance(list_circles[j], Circle):
                    print(f"{list_circles[j]} is not a circle.")
                    return
                if list_circles[j] < list_circles[i]:
                    buff = list_circles[i]
                    list_circles[i] = list_circles[j]
                    list_circles[j] = buff
        return list_circles


c1 = Circle(10, 'd')
c2 = Circle(2,'r')
print(round(c1.area(),2))
print(round(c2.area(),2))
print(c1 + c2)
print(c1 > c2)
print(c1 == c2)
c3 = Circle(1,'r')
liste =[c1, c2, c3]
print(liste)
print(Circle.sort_list(liste))