
def get_last_element(lst):
    """ Prints the last element of a given non-empty list. """
    print("The Last element in the list is:", lst[-1])

def main():
    # Ask the user how many elements they want to input
    n = int(input("Enter the number of elements in the list: "))
    lst = []

    for i in range(n):
        element = input(f"Enter element {i+1}: ")
        lst.append(element)  # Add the element to the list

    # Function call to print the last element
    get_last_element(lst)

# Required line to run the program
if __name__ == '__main__':
    main()
