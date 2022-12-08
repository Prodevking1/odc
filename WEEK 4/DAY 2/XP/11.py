sandwich_orders = [
    "Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich",
    "Pastrami sandwich"
]

sandwich_orders.append("Pastrami sandwich")
sandwich_orders.append("Pastrami sandwich")
sandwich_orders.append("Pastrami sandwich")
print("The deli has run out of pastrami.")
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

finished_sandwiches = []
for sandwich in sandwich_orders:
    print(f"I made your {sandwich}!")
    finished_sandwiches.append(sandwich)