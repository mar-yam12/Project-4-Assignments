def add_many_numbers(numbers):
    """
    Takes in a list of numbers and returns the sum of those numbers.
    """

    total = 0
    for number in numbers:
        total += number

    return total

# There is no need to edit code beyond this point

def main():
    numbers: list[int] = [8, 10, 12, 14, 16, 18, 20]  # Make a list of numbers
    sum_of_numbers: int = add_many_numbers(numbers)  # Find the sum of the list
    print("Sum of numbers is:", sum_of_numbers)  # Print out the sum above
    

if __name__ == '__main__':
    main()