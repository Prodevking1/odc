from main import Main

def get_user_menu_choice():
        print("(g) Play a new game")
        print("(q) Show scores and exit")
        choice = input(" : ")
        if choice in ['q', 'Q']:
            return 'q'
        if choice in ['g', 'G']:
            return 'g'

def print_results(results):
    print("\nGame results:")
    print("=============")
    print(f"Wins   : {results['wins']}")
    print(f"Losses : {results['losses']}")
    print(f"Draws  : {results['draws']}")
    print("\nThank you for playing!\n")

def main():
    results = {
        'wins':0,
        'losses':0,
        'draws':0
    }
    while True:
        choice = get_user_menu_choice()
        if choice == 'q':
            print_results(results)
            break
        if choice == 'g':
            game = Game(results)
            results = game.play()

main()