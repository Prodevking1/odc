#challenge 1
number = int(input("Enter a number: "))
length = int(input("Enter the length of the list: "))

result = []

for i in range(1, length+1):
    result.append(number * i)

print(result)

#challenge 2
user_word = input("Enter a word: ")
new_word = ""
for i in range(len(user_word)):
    if i == 0 or user_word[i] != user_word[i-1]:
        new_word += user_word[i]

print(new_word)

    