# Constants
SENTENCE_START = "Code in Place is fun. I learned to program and used Python to make my"

def main():
    # Prompt the user for an adjective, noun, and verb
    adjective = input("\033[1;3mPlease type an adjective and press enter:\033[0m ")
    noun = input("\033[1;3mPlease type a noun and press enter:\033[0m ")
    verb = input("\033[1;3mPlease type a verb and press enter:\033[0m ")
    
    # Construct the sentence
    sentence = f"{SENTENCE_START} {adjective} {noun} {verb}!"
    
    # Print the fun sentence
    print(sentence)

# Call the main function
if __name__ == "__main__":
    main()
