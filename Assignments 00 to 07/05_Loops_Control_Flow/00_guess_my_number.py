import random

def main():
    # Generate a random number between 0 and 99
    number = random.randint(0, 99)
    
    # Initialize guess
    guess = -1
    
    print("I am thinking of a number between 0 and 99...")
    
    # Loop until the correct guess is made
    while guess != number:
        # Ask the user for a guess
        guess = int(input("Enter a guess: "))
        
        # Provide feedback to the user
        if guess > number:
            print("Your guess is too high")
        elif guess < number:
            print("Your guess is too low")
        else:
            print(f"Congrats! The number was: {number}")

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()
