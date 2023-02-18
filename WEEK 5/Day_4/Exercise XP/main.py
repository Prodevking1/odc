# Exercise 1 : Random Sentence Generator
import random

with open('read.txt') as f:
   thesaurus = f.read().splitlines()

def get_words_from_file(num):
   '''Returns num words from thesaurus, as a list'''
   return random.choices(thesaurus, k = num)

def get_random_sentence(length):
   return (' '.join(get_words_from_file(length))).lower()

def main():
   '''This program builds a sentence with a number of words extracted randomly from a thesaurus.
   The number is specified by the user.'''
   while True:
      input_str = input("Please enter an integer between 2 and 20 (Just press <Enter> to stop the program): ")
      if len(input_str) == 0: 
         print("End of program. Thanks for playing.")
         return
      try:
         if 1 < int(input_str) < 21:
            print(get_random_sentence(int(input_str)))
      except:
         print("Invalid input")
         continue

if __name__ == "__main__":
   main()      

# Exercise 2 : Working with JSON
import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

my_dict = json.loads(sampleJson)
print("salary = " + str(my_dict['company']['employee']['payable']['salary']))
my_dict['company']['employee']['birth_date'] = None
print(my_dict)

with open('data.json', 'w') as f:
   json.dump(my_dict, f)