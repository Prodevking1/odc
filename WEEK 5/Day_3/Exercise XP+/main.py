import datetime
# Exercise 1 : 
print('\nExercise 1 : \n=================')
today = datetime.date.today()
print("Today's date:", today)

print('\nExercise 2 : \n=================')
present = datetime.datetime.now()
future = datetime.datetime(2022,1,1,0,0,0)
diff = future - present
days, hours, minutes = diff.days, diff.seconds // 3600, diff.seconds // 60 % 60
print(f"The 1st of January is in {days} days, {hours} hours and {minutes} minutes.")

print('\nExercise 3 : \n=================')
# Create a function that accepts a birthdate as an argument (in the format of your choice), then display a message stating how many minutes the user has been alive.
yyyy = int(input("Enter your birth year (4 digits): "))
m = int(input("Enter your birth month (between 1 and 12): "))
d = int(input("Enter your birth day (between 1 and 28/29/30/31): "))
hr = int(input("Enter your birth hour (between 0 and 23): "))

birthdate = datetime.datetime(yyyy,m,d,hr,0,0)
delta = present - birthdate
days, hours, minutes = delta.days, delta.seconds // 3600, delta.seconds // 60 % 60
print(f"You've been alive for {days} days, {hours} hours and {minutes} minutes.\n")

print('\nExercise 5 : \n=================')
earth_year = 31557600 # seconds
revol = {
    'Earth': 1,
    'Mercury': 0.2408467,
    'Venus': 0.61519726,
    'Mars': 1.8808158,
    'Jupiter': 11.862615,
    'Saturn': 29.447498,
    'Uranus': 84.016846,
    'Neptune': 164.79132,
}
age_s = int(input("Enter your age in seconds : "))
age_y = age_s / earth_year
print("that would be : ")
for planet in revol:
    print(f"{round(revol[planet]*age_y, 2)} {planet} years.")

print('\nExercise 6 : \n=================')
from faker import Faker

users = []
faker = Faker()
for i in range(10):
    name = faker.name()
    address = faker.address()
    language_code = faker.language_code()
    set = {'name': name, 'address': address, 'langage_code': language_code}
    print(set)
    users.append(set)