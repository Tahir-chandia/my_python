C=299792458 # speed of light in m/s

def main():
    #Enter mass to caculate energy by using  Einstein's mass-energy formula
    mass_in_kg:float = float(input("Enter mass in kg: "))
    # Calculate  Einstein's mass-energy 
    energy:float = mass_in_kg * (C ** 2)
    # Einstein's mass-energy formula
    print("e = m * C^2...")
    # Print mass in kg
    print(f"m = {mass_in_kg} kg ")
    # Print speed of light 
    print(f"C = {C} m/s ")
    # Print joules of energy 
    print(f"{energy} joules of energy!")

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()