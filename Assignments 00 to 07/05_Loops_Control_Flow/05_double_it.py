def main():
    curr_value = int(input("Enter a number: "))
    
    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value, end=" ")

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()
