
MAX_LENGTH = 3  # Define the maximum allowed length

def shorten(lst):
    while len(lst) > MAX_LENGTH:  # Check if the list length is greater than MAX_LENGTH
        removed_item = lst.pop()  # Last element remove karo
        print("Removed:", removed_item)  # Print the removed item

def main():
    lst = []  # Initialize an empty list
    
    # Ask the user how many elements they want to input
    n = int(input("Enter number of elements in the list: "))
    for _ in range(n):
        value = input("Enter a value: ")
        lst.append(value)

    print("Original list:", lst)  # Print the original list
    shorten(lst)  # Call the shorten function
    print("Shortened list:", lst)  # Print the shortened list


if __name__ == '__main__':
    main()
