def main():
    # Initialize an empty list to store the values
    values_list = []
    
    while True:
        # Prompt the user to enter a value
        value = input("Enter a value: ")
        
        # If the user presses enter without typing anything, stop the loop
        if value == "":
            break
        
        # Add the entered value to the list
        values_list.append(value)
    
    # Print the final list after the loop ends
    print("Here's the list:", values_list)

if __name__ == '__main__':
    main()
