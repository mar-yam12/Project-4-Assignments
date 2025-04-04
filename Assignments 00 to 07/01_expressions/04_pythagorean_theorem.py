
import math  

def main():
     # Prompt the user for the lengths of the two perpendicular sides
    ab = float(input("\033[1m\033[3mEnter the length of AB:\033[0m "))  
    ac = float(input("\033[1m\033[3mEnter the length of AC:\033[0m "))  
    # Calculate the length of the hypotenuse
    bc = math.sqrt(ab**2 + ac**2)  
    # Print the results
    print(f"The length of BC (the hypotenuse) is: {bc}")  

if __name__ == '__main__':
    main()
