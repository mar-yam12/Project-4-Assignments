def main():
    # Ask the user for an initial number
    start = int(input("Enter a number: "))
    
    # Initialize curr_value
    curr_value = start * 2
    
    # Keep doubling and printing until value is 100 or more
    while curr_value < 100:
        print(curr_value, end=" ")
        curr_value = curr_value * 2

    # Print the final value (which is >= 100)
    print(curr_value)

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()
