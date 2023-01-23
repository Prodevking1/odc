brand = {
"name": "Zara",
"creation_date": 1975,
"creator_name": "Amancio Ortega Gaona ",
"type_of_clothes": ["men", "women", "children", "home" ],
"international_competitors": ["Gap", "H&M", "Benetton"], 
"number_stores": 7000,
"major_color":{
    "France": "blue",
    "Spain": "red",
    "US": ["pink", "green"]
    }
}

brand["number_stores"] = 2
print("Zaras clients are:")
for i in brand["type_of_clothes"]:
    print(i, end=' ')

brand["country_creation"] = "Spain"

k = "international_competitors"
 
if k in brand:
    brand[k].append("Desigual")

del brand["creation_date"]

print("the last international competitor are ",brand["international_competitors"][-1])
print("the major clothes colors in the US are ")
for i in brand["major_color"]["US"]:
    print(i, end=' ')
    

print("the amount of key value pairs are ",len(brand))
print("\n thekeys of dictionary are ")
for i in brand.keys():
    print(i, end=' ')
    
more_on_zara = {"creation_date": 1975, "number_stores": 10000}

brand.update(more_on_zara)

print(brand["number_stores"])