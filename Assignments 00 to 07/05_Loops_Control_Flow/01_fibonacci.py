def main():
    MAX_VALUE = 10000  # Maximum value for Fibonacci terms
    
    # Starting values for Fibonacci sequence
    fib0, fib1 = 0, 1
    
    # Print the first two Fibonacci numbers
    print(fib0, end=" ")
    
    # Print the Fibonacci sequence until the next term exceeds MAX_VALUE
    while fib1 < MAX_VALUE:
        print(fib1, end=" ")
        fib0, fib1 = fib1, fib0 + fib1  # Update Fibonacci numbers

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()
