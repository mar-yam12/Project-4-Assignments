def main():
    # Dictionary storing gravity factors relative to Earth
    gravity = {
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupiter": 2.36,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.14
    }

    # Ask the user for their Earth weight
    earth_weight = float(input("Enter a weight on Earth: "))

    # Ask the user to choose a planet
    planet = input("Enter a planet: ")

    # Calculate weight on the chosen planet
    if planet in gravity:
        planet_weight = earth_weight * gravity[planet]
        rounded_weight = round(planet_weight, 2)
        print(f"The equivalent weight on {planet}: {rounded_weight}")
    else:
        print("Unknown planet. Please enter a valid planet name.")

# Call the main function
if __name__ == '__main__':
    main()
