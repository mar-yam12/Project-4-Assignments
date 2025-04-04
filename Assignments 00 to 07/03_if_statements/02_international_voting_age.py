def check_voting_eligibility(age):
    # Define the voting age for each country
    peturksbouipo_age = 16
    stanlau_age = 25
    mayengua_age = 48

    # Check if the user can vote in each country
    if age >= peturksbouipo_age:
        print(f"You can vote in Peturksbouipo where the voting age is {peturksbouipo_age}.")
    else:
        print(f"You cannot vote in Peturksbouipo where the voting age is {peturksbouipo_age}.")

    if age >= stanlau_age:
        print(f"You can vote in Stanlau where the voting age is {stanlau_age}.")
    else:
        print(f"You cannot vote in Stanlau where the voting age is {stanlau_age}.")

    if age >= mayengua_age:
        print(f"You can vote in Mayengua where the voting age is {mayengua_age}.")
    else:
        print(f"You cannot vote in Mayengua where the voting age is {mayengua_age}.")

def main():
    # Prompt the user for their age
    age = int(input("\033[34mHow old are you? \033[0m"))
    check_voting_eligibility(age)

# Call the main function to run the program
if __name__ == "__main__":
    main()
