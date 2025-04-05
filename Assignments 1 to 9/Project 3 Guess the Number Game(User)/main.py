def main():
    print("Think of a number between 1 and 100, and I'll try to guess it!")
    input("Press Enter when you're ready...")

    low = 1
    high = 100
    attempts = 0

    while True:
        guess = (low + high) // 2
        attempts += 1
        print(f"My guess is: {guess}")

        feedback = input("Is it (h)igh, (l)ow, or (c)orrect? ").lower()

        if feedback == 'c':
            print(f"🎉 Yay! I guessed your number in {attempts} tries.")
            break
        elif feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        else:
            print("Please enter 'h', 'l', or 'c' only.")

# Required to run main function
if __name__ == '__main__':
    main()
