matrix = [    ["7", "i", "3"],
    ["T", "s", "i"],
    ["h", "%", "x"],
    ["i", " ", "#"],
    ["s", "M", " "],
    ["$", "a", " "],
    ["#", "t", "%"],
    ["^", "r", "!"]
]
secret = ""

for line in matrix:
    for i in range(len(line)):
        if not line[i].isalpha():
            line[i] = " "

for i in range(len(matrix[0])):
    for line in matrix:
        if line == matrix[0]:
            if not line[i] == " ":
                secret += line[i]
        else:
            if line[i] != " ":
                secret += line[i]
            else:
                secret += " "

secret = " ".join(secret.split())
print(secret)
