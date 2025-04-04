def main():
    print("This File is a Python Script that creates a bot that agrees with the user")

    # Get the user's input
    animal = input("\033[1;3m What's your favorite Animal? \033[0m")

    # Print the bot's input
    print(f"My favorite animal is also \033[1m\033[3m\033[35m{animal.upper()} \033[0m")

if __name__ == "__main__":
    main()


