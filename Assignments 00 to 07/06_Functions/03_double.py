def double(num):
    return num * 2

def main():
    user_input = input("Enter a number: ")
    number = int(user_input)
    result = double(number)
    print(f"Double that is: {result}")

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()
