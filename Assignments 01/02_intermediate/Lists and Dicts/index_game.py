def access_element(my_list, index):
    if 0 <= index < len(my_list):
        return my_list[index]
    else:
        return "Index out of range!"

def modify_element(my_list, index, new_value):
    if 0 <= index < len(my_list):
        my_list[index] = new_value
        return my_list
    else:
        return "Index out of range!"

def slice_list(my_list, start, end):
    if 0 <= start <= end <= len(my_list):
        return my_list[start:end]
    else:
        return "Invalid slice range!"

def game():
    my_list = ["apple", "banana", "cherry", "date", "elderberry"]
    print("Current list:", my_list)

    while True:
        print("\nChoose an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            index = int(input("Enter index to access: "))
            result = access_element(my_list, index)
            print("Result:", result)

        elif choice == '2':
            index = int(input("Enter index to modify: "))
            new_value = input("Enter new value: ")
            result = modify_element(my_list, index, new_value)
            print("Updated list:", result)

        elif choice == '3':
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            result = slice_list(my_list, start, end)
            print("Sliced list:", result)

        elif choice == '4':
            print("Thanks for playing!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    game()
