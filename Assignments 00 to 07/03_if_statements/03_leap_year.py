def is_leap_year(year):
    # Check if the year is divisible by 4, but not by 100, unless it's divisible by 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def main():
    # Ask the user for the year
    year = int(input("Enter a year: "))

    # Check if the year is a leap year
    if is_leap_year(year):
        print("That's a leap year!")
    else:
        print("That's not a leap year.")

# Run the program
if __name__ == "__main__":
    main()
