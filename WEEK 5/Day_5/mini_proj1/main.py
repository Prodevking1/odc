import random
class Main():
    def __init__(self, results):
        self.results = results

    def get_user_item(self):
        while True:
            select = input("select (r)ock, (p)aper or (s)cissors: ")
            if select in ['r', 'R', 'p', 'P', 's', 'S']:
                return select.lower()

    def get_computer_item(self):
        return random.choice(['r', 'p', 's'])

    def get_game_result(self, user_item, computer_item):
        win_config = (('r', 's'), ('p', 's'), ('s','p'))
        corr = {'r':'rock', 'p':'paper', 's':'scissors'}
        if (user_item, computer_item) in win_config:
            result = "You win!"
            self.results['wins'] += 1
        elif user_item == computer_item:
            result = "It is a draw!"
            self.results['draws'] += 1
        else:
            result = "Computer wins!"
            self.results['losses'] += 1
        print(f"You chose {corr[user_item]}. Computer chose {corr[computer_item]}. {result}\n")
        return self.results

    def play(self):
        return(self.get_game_result(self.get_user_item(), self.get_computer_item()))