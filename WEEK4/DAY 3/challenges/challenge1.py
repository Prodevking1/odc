word = input("Enter a word: ")

indexes = {}

for i in range(len(word)):
    letter = word[i]

    if letter not in indexes:
        indexes[letter] = []

    indexes[letter].append(i)

print(indexes)
