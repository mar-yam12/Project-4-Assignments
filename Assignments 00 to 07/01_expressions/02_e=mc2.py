# Constant for the speed of light in meters per second
C: int = 299792458 # speed of light in m/s

def main():
    # Prompt the user for the mass
    mass_in_kg = float(input("Enter kilos of mass: "))

    # Calculate the energy using the formula E = m * c^2
    energy_in_joules = mass_in_kg * (C ** 2)

    # Print the results
    print("\ne = m * C^2...")
    print(f"m = {mass_in_kg} kg")
    print(f"C = {C} m/s")
    print(f"{energy_in_joules} joules of energy!\n")


if __name__ == "__main__":
    main()