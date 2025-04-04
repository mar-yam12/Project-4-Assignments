def add_three_copies(my_list, data):
    """Adds three copies of the data to the provided list"""
    my_list.append(data)
    my_list.append(data)
    my_list.append(data)

def main():
    # Get user input for the message
    message = input("Enter a message to copy: ")
    
    # Initialize an empty list
    my_list = []
    
    # Print the list before adding the copies
    print("List before:", my_list)
    
    # Call the function to add three copies of the message to the list
    add_three_copies(my_list, message)
    
    # Print the list after adding the copies
    print("List after:", my_list)

if __name__ == '__main__':
    main()
