def calculate_atoms(substance_mass_grams, molar_mass_grams_per_mole):
    # Calculate the number of moles
    moles = substance_mass_grams / molar_mass_grams_per_mole
    
    # Use Avogadro's number to calculate the number of atoms
    avogadro_number = 6.022e23
    atoms = moles * avogadro_number
    
    return atoms

if __name__ == "__main__":
    substance_mass_grams = float(input("Enter the mass of the substance in grams: "))
    molar_mass_grams_per_mole = float(input("Enter the molar mass of the substance in grams per mole: "))
    
    num_atoms = calculate_atoms(substance_mass_grams, molar_mass_grams_per_mole)
    
    print(f"The number of atoms in the object is approximately {num_atoms:.2e}")
