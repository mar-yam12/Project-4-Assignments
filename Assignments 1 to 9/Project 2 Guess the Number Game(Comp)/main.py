import random

def main():
    print("🎮 Welcome to the Guess the Number Game! 🎲")
    print("🤔 I'm thinking of a number between 1 and 100...")

    # Computer picks a random number between 1 and 100
    secret_number = random.randint(1, 100)
    guess = None
    attempts = 0

    while guess != secret_number:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("⬇️ Too low! Try again.")
            elif guess > secret_number:
                print("⬆️ Too high! Try again.")
            else:
                print(f"🎉 Congrats! You guessed it in {attempts} tries. The number was: {secret_number} 🏆")
        except ValueError:
            print("❌ Please enter a valid number!")

# Required to run main function
if __name__ == '__main__':
    main()
