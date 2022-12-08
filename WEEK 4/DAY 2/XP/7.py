fruits = input("Your favorite fruits: ")
list = fruits.split(" ")
choice = input("Which fruit do you want to chose?:  ")
if choice in list:
    print("You chose one of your favorite fruits! Enjoy!"
          )
else:
    print("You chose a new fruit. I hope you enjoy it too!")