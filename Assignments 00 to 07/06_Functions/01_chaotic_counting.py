import random

# Probability that done() returns True (feel free to adjust)
DONE_LIKELIHOOD = 0.3

def done():
    return random.random() < DONE_LIKELIHOOD

def chaotic_counting():
    for i in range(1, 11):
        if done():
            return
        print(i)

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'm done.")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
