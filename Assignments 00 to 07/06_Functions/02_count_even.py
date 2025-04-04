def count_even(lst):
    # Prompt user until they press enter (blank input)
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":
            break
        lst.append(int(user_input))

    # Count how many numbers in the list are even
    even_count = 0
    for num in lst:
        if num % 2 == 0:
            even_count += 1

    # Print the number of even values
    print(f"Number of even numbers: {even_count}")

def main():
    lst = []
    count_even(lst)

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()
