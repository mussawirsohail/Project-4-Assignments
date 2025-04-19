C = 299_792_458  # m/s

def main():
    while True:
        try:
            mass = float(input("Enter kilos of mass: "))
            
            print("\ne = m * C^2...\n")
            print(f"m = {mass} kg")
            print(f"C = {C} m/s\n")

            # Calculate energy
            energy = mass * C**2

            # Output result
            print(f"{energy} joules of energy!\n")

        except ValueError:
            print("Please enter a valid number for mass.\n")

if __name__ == "__main__":
    main()
