from anagram_check import AnagramChecker


def main():
    print("\nWelcome to Anagram Checker!")
    while True:
        inp_str = input("\nPlease enter a word in lowercase (just hit <Enter> to exit) : ")
        if len(inp_str) == 0:
            print("\nThanks for playing. Goodbye.\n")
            break
        inp_str = inp_str.strip()
        if not(inp_str.isalpha() and inp_str.islower() and len(inp_str.split()) == 1):
            print("Sorry, unexpected entry. Try again.")
            continue
        
        run = AnagramChecker()
        anagrams = run.get_anagrams(inp_str)
        print(f"\nYOUR WORD : '{inp_str}'")
        print("A valid word indeed.")
        if anagrams == []:
            nice_str = 'none'
        else:
            nice_str = ', '.join(anagrams)
        print(f"Anagrams for this word : {nice_str}.")

main()
        