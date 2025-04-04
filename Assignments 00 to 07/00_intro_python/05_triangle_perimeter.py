def main():
    # Prompt user for the lengths of the sides of the triangle
    side1 = float(input("\033[1;3m Enter the length of side 1: \033[0m"))
    side2 = float(input("\033[1;3m Enter the length of side 2: \033[0m"))
    side3 = float(input("\033[1;3m Enter the length of side 3: \033[0m"))

    # Calculate the perimeter of the triangle
    perimeter = side1 + side2 + side3

    # Print the perimeter of the triangle
    print(f"The perimeter of the triangle is \033[34m{perimeter}\033[0m")


if __name__ == "__main__":
    main()

