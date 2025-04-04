def main():
    # Initialize an empty phonebook dictionary
    phonebook = {}

    while True:
        # Show a simple menu for the user to choose an action
        print("\nPhonebook Menu:")
        print("1. Add Contact")
        print("2. Lookup Contact")
        print("3. Delete Contact")
        print("4. View All Contacts")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':  # Add a new contact
            name = input("Enter the contact's name: ")
            number = input("Enter the contact's phone number: ")
            phonebook[name] = number
            print(f"Contact {name} added successfully!")

        elif choice == '2':  # Lookup a contact
            name = input("Enter the name of the contact to look up: ")
            if name in phonebook:
                print(f"The phone number for {name} is {phonebook[name]}")
            else:
                print(f"Contact {name} not found.")

        elif choice == '3':  # Delete a contact
            name = input("Enter the name of the contact to delete: ")
            if name in phonebook:
                del phonebook[name]
                print(f"Contact {name} deleted successfully.")
            else:
                print(f"Contact {name} not found.")

        elif choice == '4':  # View all contacts
            if phonebook:
                print("\nPhonebook Contacts:")
                for name, number in phonebook.items():
                    print(f"{name}: {number}")
            else:
                print("Your phonebook is empty.")

        elif choice == '5':  # Exit the program
            print("Exiting the phonebook. Goodbye!")
            break

        else:
            print("Invalid option. Please choose a valid number between 1 and 5.")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
