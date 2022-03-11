import random

class cardKnockout():
    suffle_deck = []
    player_1 = []
    player_2 = []
    count_p1 = 0
    count_p2 = 0
    tie = 0

    def __init__(self) -> None:
        self.split_deck()
        self.run_game()
        self.show_result()
    
    def reset_game(self) -> None:
        self.suffle_deck = []
        self.player_1 = []
        self.player_2 = []
        self.count_p1 = 0
        self.count_p2 = 0
        self.tie = 0

    def generate_suffle_deck(self) -> list:
        card_list = list(range(1, 14))
        deck = card_list * 4
        random.shuffle(deck)

        return deck

    def split_deck(self) -> None:
        deck = self.generate_suffle_deck()
        self.player_1 = deck[0:26]
        self.player_2 = deck[26:]

    def run_game(self) -> None:
        for i in range(len(self.player_1)):
                if self.player_1[i] > self.player_2[i]:
                    self.count_p1 = self.count_p1 + 1
                elif self.player_2[i] > self.player_1[i]:
                    self.count_p2 = self.count_p2 + 1
                else:
                    self.tie += self.tie

        print(self.count_p1)
        print(self.count_p2)
        print(self.tie)

    def show_result(self) -> None:
        if self.count_p1 > self.count_p2:
            print("Wins player 1.")
        elif self.count_p2 > self.count_p1:
            print("Wins player 2.")
        else:
            print("It's a tie.")
