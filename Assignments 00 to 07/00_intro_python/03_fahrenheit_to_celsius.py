def main():
    # Prompt user for temperature in Fahrenheit
    degrees_fahrenheit = float(input("Enter temperature in Fahrenheit: "))

    # Convert Fahrenheit to Celsius
    degrees_celsius = (degrees_fahrenheit - 32) * 5.0 / 9.0

    # Print the result
    print(f"Temperature: {degrees_fahrenheit}F = {degrees_celsius}C")


if __name__ == '__main__':
    main() 