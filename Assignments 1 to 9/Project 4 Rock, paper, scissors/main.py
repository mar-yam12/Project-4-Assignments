import random

def main():
    print("🎮 Welcome to Rock, Paper, Scissors!")
    choices = ['rock', 'paper', 'scissors']

    while True:
        user_choice = input("Choose rock, paper, or scissors (or type 'quit' to exit): ").lower()

        if user_choice == 'quit':
            print("Thanks for playing! 👋")
            break

        if user_choice not in choices:
            print("❌ Invalid choice. Please try again.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer choose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a draw! 😐")
        elif (
            (user_choice == 'rock' and computer_choice == 'scissors') or
            (user_choice == 'scissors' and computer_choice == 'paper') or
            (user_choice == 'paper' and computer_choice == 'rock')
        ):
            print("You win! 🎉")
        else:
            print("You lose! 😢")

        print()  # Blank line for spacing

# Required to run main function
if __name__ == '__main__':
    main()
