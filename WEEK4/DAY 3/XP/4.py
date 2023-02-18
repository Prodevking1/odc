users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

# Recreate the first result
disney_users_A = {}
for i, name in enumerate(users):
    disney_users_A[name] = i
print(disney_users_A)

# Recreate the second result
disney_users_B = {}
for i, name in enumerate(users):
    disney_users_B[i] = name
print(disney_users_B)

disney_users_C = dict(sorted({name: i for i, name in enumerate(users)}.items()))
print(disney_users_C)

# Recreate the first result for characters with "i" in their name
disney_users_A_i = {}
for i, name in enumerate(users):
    if "i" in name:
        disney_users_A_i[name] = i
print(disney_users_A_i)

# Recreate the first result for characters with names starting with "m" or "p"
disney_users_A_mp = {}
for i, name in enumerate(users):
    if name[0] in ["m", "p"]:
        disney_users_A_mp[name] = i
print(disney_users_A_mp)
