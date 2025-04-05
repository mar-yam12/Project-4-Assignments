def main():
    print("🎮 Welcome to the Mad Libs game! 🎲 Please provide the following words:")

    name = input("Enter a name: ")
    place = input("Enter a place: ")
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    animal = input("Enter an animal: ")
    food = input("Enter a type of food: ")

    print("\n📖 Here's your Mad Libs story: 📖\n")
    print(f"One day, {name} went to {place} feeling very {adjective}. 🌟")
    print(f"They brought their favorite {noun} and decided to {verb} with a {animal}. 🐾")
    print(f"After a long day, they enjoyed some delicious {food} before heading home. 🍽️")
    print("It was truly a day to remember! ✨")

# Required to run main function
if __name__ == '__main__':
    main()
