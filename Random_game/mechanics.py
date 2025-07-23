import random
from queue import PriorityQueue


class Game:

    def __init__(self, guesses, attempts,ask=None):
        self.secret_number =random.randint(1,100)
        self.guesses = guesses
        self.attempt = attempts
        self.ask = ask

    def play_game(self):
        self.guesses = []
        self.attempt = 0

    def ask_user(self):
        try:
            self.ask= int(input("Guess the number: "))
            self.guesses.append(self.ask)
            self.attempt += 1
            return self.ask
        except ValueError:
            print("Invalid input, please try again.")
            return None










