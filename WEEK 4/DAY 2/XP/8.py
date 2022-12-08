toppings = []
base_price = 10
topping = input(
    "Entrez une garniture de pizza (ou tapez 'quit' pour arrêter) : ")
while topping != "quit":
    toppings.append(topping)
    print("Nous ajouterons la garniture '" + topping + "' à votre pizza.")
    topping = input(
        "Entrez une garniture de pizza (ou tapez 'quit' pour arrêter) : ")
print("Voici les garnitures de votre pizza :")
for topping in toppings:
    print("- " + topping)
total_price = base_price + (len(toppings) * 2.5)
print("Le prix total de votre pizza est de " + str(total_price) + "$.")
