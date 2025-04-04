
def main():
    # Ask the user for two numbers
    numerator: int = int(input("\033[1;3mPlease enter an integer to be divided:\033[0m "))  
    denominator: int = int(input("\033[1;3mPlease enter an integer to divide by:\033[0m "))  

    # Calculate the quotient and remainder
    quotient: int = numerator // denominator
    remainder: int = numerator % denominator

    # Print the results
    print(f"The result of this division is {quotient} with a remainder of {remainder}")

if __name__ == '__main__':
    main()
