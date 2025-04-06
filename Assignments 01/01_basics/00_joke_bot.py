# Constants
PROMPT = "What do you want? "
JOKE = ("Here is a joke for you! 😂 Why do Java developers wear glasses? "
        "Because they don't C#! 🤓")
SORRY = "Sorry I only tell jokes 🤖"

def main():
    user_input = input(PROMPT)
    if user_input == "Joke":
        print(JOKE)
    else:
        print(SORRY)

if __name__ == '__main__':
    main()
