import random

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
