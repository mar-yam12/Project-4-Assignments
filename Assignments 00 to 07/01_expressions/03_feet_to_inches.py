# Constants
FEET_IN_INCHES: int = 12 # conversion factor

def main():
    # Prompt the user for the number of feet
    feet = float(input("Enter the number of feet: "))

    # Calculate the number of inches
    inches = feet * FEET_IN_INCHES

    # Print the results
    print(f"That is {inches} inches!")


if __name__ == "__main__":
    main()

