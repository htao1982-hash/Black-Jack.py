import random
from art import tprint, art

class CardDeck:
    # manage card
    def __init__(self):
        self.cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    def draw(self):
       return random.choice(self.cards)

class BlackjackGame:
    def __init__(self):
        self.deck = CardDeck()
        self.user_cards = []
        self.computer_cards = []
        self.is_game_over = False

    def calculate_score(self, hand):
        if sum(hand) == 21 and len(hand) == 2:
            return 0

        score = sum(hand)
        while score > 21 and 11 in hand:
            hand.remove(11)
            hand.append(1)
            score = sum (hand)
        return score

    def start_new_round(self):
        tprint("BLACKJACK")
        self.user_cards = [self.deck.draw(), self.deck.draw()]
        self.computer_cards = [self.deck.draw(), self.deck.draw()]
        self.is_game_over = False
        self.play_user_turn()

    def play_user_turn(self):
        while not self.is_game_over:
            u_score = self.calculate_score(self.user_cards)
            c_score = self.calculate_score(self.computer_cards)

            print(f"Your cards: {self.user_cards}, current score:{u_score}")
            print(f"Computer's card:{self.computer_cards[0]}")
            if u_score > 21:
                print("You went over! You lose!")
                self.is_game_over = True
                break
            if u_score == 0 or c_score > 21:
                self.is_game_over = True
                break
            else:
                choice = input("Type 'y' to get another card, 'n' to pass: ")
                if choice == 'y':
                    self.user_cards.append(self.deck.draw())
                else:
                    self.is_game_over = True

            self.play_computer_turn()

    def play_computer_turn(self):
        c_score = self.calculate_score(self.computer_cards)
        while c_score != 0 and c_score < 17:
            self.computer_cards.append(self.deck.draw())
            c_score = self.calculate_score(self.computer_cards)

        self.show_final_result()

    def show_final_result(self):
        u_score = self.calculate_score(self.user_cards)
        c_score = self.calculate_score(self.computer_cards)

        print(f"Final hand: {self.user_cards}, score: {u_score}")
        print(f"Computer hand: {self.computer_cards}, score: {c_score}")

        if u_score > 21:
            print("You went over. You lose!")
        elif c_score > 21:
            print("Opponent went over. You win!")
            print(art("money4"))
        elif u_score == c_score:
            print("Draw!")
        elif u_score > c_score:
            print("You win!")
            print(art("money4"))
        else:
            print("You lose!")

game = BlackjackGame()

while input("Do you want to play? 'y' or 'n': ") == 'y':
     game.start_new_round()
