def get_first_element(lst):
    """Prints the first element of the given list"""
    print("The First element in the list is:", lst[0])

def main():
    # Initialize an empty list
    lst = []

    # Ask the user how many elements they want to input
    num_elements = int(input("How many elements would you like to add to the list? "))

    # Prompt the user to input the elements one at a time
    for _ in range(num_elements):
        element = input("Enter an element: ")
        lst.append(element)  # Add the element to the list

    # Call the function to print the first element of the list
    get_first_element(lst)

if __name__ == '__main__':
    main()
