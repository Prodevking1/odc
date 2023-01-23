#float store the decimal values but int store the integer values

sequence = range(2, 10)
sequence = [i * 0.5 +0.5 for i in sequence]

def is_integer(a):
    if a % 1==0:
        return int(a)
    else:
        return a

for i in sequence:
    print(is_integer(i))
