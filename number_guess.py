import random


class NumberGuesser:
    def __init__(self, lower=1, upper=100, max_attempts=7):
        self.lower_limit = lower
        self.upper_limit = upper
        self.max_attempts = max_attempts
        self.secret_number = None
        self.attempts = 0
        self.score = 0

    def generate_number(self):
        """Generate a random secret number"""
        self.secret_number = random.randint(self.lower_limit, self.upper_limit)

    def check_guess(self, guess):
        """Check if guess is correct, return status"""
        self.attempts += 1

        if guess == self.secret_number:
            return "correct"
        elif guess < self.secret_number:
            return "low"
        else:
            return "high"

    def display_welcome(self):
        """Show game instructions"""
        print(f"\nWelcome to Number Guesser!")
        print(f"Guess a number between {self.lower_limit} and {self.upper_limit}")
        print(f"You have {self.max_attempts} attempts\n")

    def display_instructions(self):
        """Show game rules"""
        print("Type 'quit' to exit at any time")
        print("Type 'hint' for a clue (costs 1 attempt)\n")

    def run(self):
        """Main game loop"""
        self.generate_number()
        self.display_welcome()
        self.display_instructions()

        while self.attempts < self.max_attempts:
            try:
                user_input = input(f"Attempt {self.attempts + 1}/{self.max_attempts}: ")

                if user_input.lower() == 'quit':
                    print(f"Game ended. The number was {self.secret_number}")
                    return

                if user_input.lower() == 'hint':
                    hint_range = self.secret_number // 10 * 10
                    print(f"Hint: The number is between {hint_range} and {hint_range + 10}")
                    self.attempts += 1
                    continue

                guess = int(user_input)
                result = self.check_guess(guess)

                if result == "correct":
                    self.score = self.max_attempts - self.attempts + 1
                    print(f"Congratulations! You won with score {self.score}")
                    return
                else:
                    print(f"Too {result}! Try again.")

            except ValueError:
                print("Please enter a valid number or command")

        print(f"\nGame Over! The number was {self.secret_number}")


# Create and start the game
if __name__ == "__main__":
    game = NumberGuesser()
    game.run()

def number_guessing_game():

    lower_limit = 1
    upper_limit = 100
    max_attempts = 7

    print("Welcome to the number guessing game!")
    print(f"Please pick a number between {lower_limit} and {upper_limit}... ")

    secret_number = random.randint(lower_limit, upper_limit)
    attempts = 0

    while attempts < max_attempts:
        try:
            guess = int(input("\nYour Guess: "))
            attempts += 1
            if guess < lower_limit or guess > upper_limit:
                print(f"please enter a number between {lower_limit} and {upper_limit} ")
            if guess == secret_number:
                print(f"Congratulations, you guessed in {attempts} tries! ")
            elif guess < secret_number:
                print("Try higher!!")
            else:
                print("Try Lower!")

            print(f"Attempts remaining : {max_attempts - attempts}")

        except ValueError:
            print("Please enter a valid number")

    print(f"\nGame Over! The number was {secret_number}")

if __name__ == "__main__":
    number_guessing_game()
