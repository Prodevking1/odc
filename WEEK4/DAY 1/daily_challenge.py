# Demande à l'utilisateur de saisir une chaîne de caractères
string = input("Entrez une chaîne de caractères : ")

# Vérifie si la longueur de la chaîne est supérieure, inférieure ou égale à 10
if len(string) > 10:
    print("La chaîne est trop longue.")
elif len(string) < 10:
    print("La chaîne n'est pas assez longue.")
    
# Affiche le premier et le dernier caractère de la chaîne
print("Le premier caractère est :", string[0])
print("Le dernier caractère est :", string[-1])

# Affiche la chaîne caractère par caractère
result = ""
for char in string:
    result += char
    print(result)
