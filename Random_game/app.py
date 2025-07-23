from  mechanics import Game

if __name__ == "__main__":
    game = Game(guesses= [], attempts= 0)
    while True:

        user_input = game.ask_user()

        if user_input is None:
            continue

        elif user_input == game.secret_number:
            accuracy = 100 - (sum(abs(guess - game.secret_number) for guess in game.guesses) / game.attempt)
            print(f"Your are right! {user_input} is the secret number! 🥳🎆")
            print("Your guesses:", *game.guesses)
            print(f"Your attempt: {game.attempt}")
            print(f"Your accuracy: {accuracy:.2f}")

            new_game = input("Want to play again?(y/n): ").lower()
            if new_game == "y":
                game = Game(guesses= [], attempts= 0)
                continue

            else:
                print("Thanks for playing 🙏.")
                break

        elif abs(user_input - game.secret_number) <= 5:
            print("Too close!")
        elif user_input > game.secret_number:
            print("Too high, please try a bit lower.")
        else:
            print("Too low, please try a bit higher.")


