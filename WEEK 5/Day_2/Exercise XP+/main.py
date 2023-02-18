# Exercise 1 : Family
class Family():
    def __init__(self, members, last_name):
        self.members = members
        self.last_name = last_name

    def __repr__(self):
        print(f"\nThese are the members of Family {self.last_name} :\n=========================================")
        out_str = ''
        for set in self.members:
            out_str += (f"{set['name']}\n")
        return out_str

    def born(self, new_members):
        print(f"Here are the newest additions to the {self.last_name} family :\n=====================================================")
        for set in new_members:
            self.members.append(set)
            print(f"Congratulations and welcome to {set['name']}")

    def is_18(self, name):
        for set in self.members:
            if set['name'] == name:
                if set['age'] >= 18:
                    return True
                else:
                    return False
        return f"{name} not in this family."

# Exercise 2 : The Incredibles
class Below_18(Exception):
    pass


class Not_in_family(Exception):
    pass


class TheIncredibles(Family):
    def use_power(self, name):
        try:
            for dict in self.members:
                if dict['name'] == name:
                    if dict['age'] >= 18:
                        return f"{name}'s power is {dict['power']}"
                    else:
                        raise Below_18
            raise Not_in_family
        except Below_18:
            return f"{name} is under age !"
        except Not_in_family:
            return f"{name} not in this family !"
        
    def incredible_presentation(self):
        print(f"These are the members for 'special' Family {self.last_name} :\n=========================================")
        out_str = ''
        for set in self.members:
            out_str += (f"{set['name']} a.k.a. {set['incredible_name']}\n")
        return out_str

print("Exercise 1 : Family\n===================")
first_members = [
    {'name':'Michael','age':35,'gender':'Male','is_child':False},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False}
]
family1 = Family(first_members, 'Johnson')

new_members = [
    {'name':'David','age':0,'gender':'Male','is_child':True},
    {'name':'Sophie','age':0,'gender':'Female','is_child':True}
]
family1.born(new_members)

print(family1)
print("Is Sarah older than 18 ? " + str(family1.is_18('Sarah')))
print("Is Andrea older than 18 ? " + str(family1.is_18('Andrea')))

print("\nExercise 2 : The Incredibles\n============================")
incredibles_members = [
    {'name':'Bob','age':35,'gender':'Male','is_child':False,'power':'super-strength','incredible_name':'Mr. Incredible'},
    {'name':'Helen','age':32,'gender':'Female','is_child':False,'power':'stretch','incredible_name':'Elastigirl'},
    {'name':'Violet','age':14,'gender':'Female','is_child':True,'power':'invisibility & force field','incredible_name':'Violet'},
    {'name':'Dashiell','age':11,'gender':'Male','is_child':True,'power':'super-speed','incredible_name':'Dash'},   
]
family2 = TheIncredibles(incredibles_members, 'Parr')
print(family2)

incredibles_new_members = [
    {'name':'Jack-Jack','age':2,'gender':'Male','is_child':True,'power':'unknown','incredible_name':'Jack-Jack'}
    ]
family2.born(incredibles_new_members)
print(family2)
print(family2.incredible_presentation())
for m in family2.members:
    print(family2.use_power(m['name']))
print('\nEnd of program\n')