names = ["Alice", "Bob", "Charlie", "David", "Emily"]
ticket_prices = {"under_3": 0, "3_to_12": 10, "over_12": 15}
total_cost = 0
for name in names:
    age = int(input("Quel est l'âge de " + name + " ? "))
    if age < 3:
        cost = ticket_prices["under_3"]
    elif age >= 3 and age <= 12:
        cost = ticket_prices["3_to_12"]
    elif age > 12:
        cost = ticket_prices["over_12"]
    total_cost += cost
    if age < 16 or age > 21:
        names.remove(name)
print("Le coût total des billets est de " + str(total_cost) + "$.")
print("Les personnes autorisées à regarder le film sont :")
for name in names:
    print("- " + name)
