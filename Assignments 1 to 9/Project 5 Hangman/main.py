import random

# List of words to choose from
WORDS = ["python", "hangman", "programming", "challenge", "developer", "openai", "keyboard"]

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def main():
    print("Welcome to Hangman Game!🕹️")
    word_to_guess = random.choice(WORDS)
    guessed_letters = set()
    attempts = 6  # Total wrong guesses allowed

    print("\nGuess the word:")

    while attempts > 0:
        print("\n" + display_word(word_to_guess, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("❌ Please enter a single alphabetical character.")
            continue

        if guess in guessed_letters:
            print("⚠️ You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word_to_guess:
            print("✅ Good guess!")
        else:
            attempts -= 1
            print(f"❌ Wrong guess! You have {attempts} attempts left.")

        if all(letter in guessed_letters for letter in word_to_guess):
            print(f"\n🎉 Congratulations! You guessed the word: {word_to_guess}")
            break
    else:
        print(f"\n💀 Game Over! The word was: {word_to_guess}")

# Call the main function
if __name__ == '__main__':
    main()
