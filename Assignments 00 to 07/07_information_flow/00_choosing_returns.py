ADULT_AGE = 18  # Age at which someone is considered an adult in the US

def is_adult(age):
    if age >= ADULT_AGE:
        return True
    else:
        return False

def main():
    age = int(input("How old is this person?: "))
    print(is_adult(age))

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()
