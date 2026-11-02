import math


raw_kc = input("Enter the equilibrium constant Kc: ")
print("Raw input type:", type(raw_kc))

try:
    kc = float(raw_kc)
except ValueError:
    print("Invalid input: Kc must be a number.")
else:
    print("Converted value type:", type(kc))

    if not math.isfinite(kc) or kc <= 0:
        print("Invalid Kc: enter a finite number greater than 0.")
    else:
        # Kc * x**2 - (Kc + 1) * x + 0.25 * Kc = 0
        a = kc
        b = -(kc + 1)
        c = 0.25 * kc
        discriminant = b**2 - 4 * a * c

        print(f"a = {a}, b = {b}, c = {c}")
        print("Discriminant:", discriminant)

        if discriminant < 0:
            print("No real roots.")
        else:
            sqrt_discriminant = math.sqrt(discriminant)
            root1 = (-b + sqrt_discriminant) / (2 * a)
            root2 = (-b - sqrt_discriminant) / (2 * a)
            print("Root 1:", root1)
            print("Root 2:", root2)

            if 0 <= root1 <= 0.5:
                x = root1
            elif 0 <= root2 <= 0.5:
                x = root2
            else:
                print("No root satisfies the physical range 0 <= x <= 0.5.")
                x = None

            if x is not None:
                equilibrium_a = 0.5 - x
                equilibrium_b = 0.5 - x
                equilibrium_c = x
                conversion = x / 0.5 * 100

                print(f"Equilibrium [A] = {equilibrium_a:.3f} mol/L")
                print(f"Equilibrium [B] = {equilibrium_b:.3f} mol/L")
                print(f"Equilibrium [C] = {equilibrium_c:.3f} mol/L")
                print(f"Limiting-reactant conversion = {conversion:.3f}%")

                if conversion >= 70:
                    classification = "high"
                elif conversion >= 40:
                    classification = "moderate"
                else:
                    classification = "low"

                print("Conversion classification:", classification)
