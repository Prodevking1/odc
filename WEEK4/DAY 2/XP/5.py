sequence = range(1, 21)
for i in sequence:
    print(i)
    
for i in sequence:
    if i.__index__() % 2 == 0:
        print(i)