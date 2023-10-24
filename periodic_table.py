import json

elements = [
    {"symbol": "H",  "name": "Hydrogen", "atomic_number": 1, "atomic_weight": 1.008},
    {"symbol": "He", "name": "Helium", "atomic_number": 2, "atomic_weight": 4.0026},
    {"symbol": "Li", "name": "Lithium", "atomic_number": 3, "atomic_weight": 6.941},
    {"symbol": "Be", "name": "Beryllium", "atomic_number": 4, "atomic_weight": 9.0122},
    {"symbol": "B",  "name": "Boron", "atomic_number": 5, "atomic_weight": 10.8117},
    {"symbol": "C",  "name": "Carbon", "atomic_number": 6, "atomic_weight": 12.0107},
    {"symbol": "N",  "name": "Nitrogen", "atomic_number": 7, "atomic_weight": 14.0067},
    {"symbol": "O",  "name": "Oxygen", "atomic_number": 8, "atomic_weight": 15.9994},
    {"symbol": "F",  "name": "Fluorine", "atomic_number": 9, "atomic_weight": 18.998},
    {"symbol": "Ne", "name": "Neon", "atomic_number": 10, "atomic_weight": 20.1797},
    {"symbol": "Na", "name": "Sodium", "atomic_number": 11, "atomic_weight": 22.9897},
    {"symbol": "Mg", "name": "Magnesium", "atomic_number": 12, "atomic_weight": 24.3051},
    {"symbol": "Al", "name": "Aluminium", "atomic_number": 13, "atomic_weight": 26.9815},
    {"symbol": "Si", "name": "Silicon", "atomic_number": 14, "atomic_weight": 28.0855},
    {"symbol": "P",  "name": "Phosphorus", "atomic_number": 15, "atomic_weight": 30.9737},
    {"symbol": "S",  "name": "Sulfur", "atomic_number": 16, "atomic_weight": 32.063},
    {"symbol": "Cl", "name": "Chlorine", "atomic_number": 17, "atomic_weight": 35.4533},
    {"symbol": "Ar", "name": "Argon", "atomic_number": 18, "atomic_weight": 39.9482},
    {"symbol": "K",  "name": "Potassium", "atomic_number": 19, "atomic_weight": 39.0983},
    {"symbol": "Ca", "name": "Calcium", "atomic_number": 20, "atomic_weight": 40.0786},
    {"symbol": "Sc", "name": "Scandium", "atomic_number": 21, "atomic_weight": 44.9559},
    {"symbol": "Ti", "name": "Titanium", "atomic_number": 22, "atomic_weight": 47.8673},
    {"symbol": "V",  "name": "Vanadium", "atomic_number": 23, "atomic_weight": 50.9415},
    {"symbol": "Cr", "name": "Chromium", "atomic_number": 24, "atomic_weight": 51.9961},
    {"symbol": "Mn", "name": "Mendelevium", "atomic_number": 25, "atomic_weight": 54.9380},
    {"symbol": "Fe", "name": "Iron", "atomic_number": 26, "atomic_weight": 55.8455},
    {"symbol": "Co", "name": "Cobalt", "atomic_number": 27, "atomic_weight": 58.9331},
    {"symbol": "Ni", "name": "Nickel", "atomic_number": 28, "atomic_weight": 58.6934},
    {"symbol": "Cu", "name": "Copper", "atomic_number": 29, "atomic_weight": 63.5469},
    {"symbol": "Zn", "name": "Zinc", "atomic_number": 30, "atomic_weight": 65.38},
    {"symbol": "Ga", "name": "Gallium", "atomic_number": 31, "atomic_weight": 69.9050},
    {"symbol": "Ge", "name": "Germanium", "atomic_number": 32, "atomic_weight": 72.630},
    {"symbol": "As", "name": "Arsenic", "atomic_number": 33, "atomic_weight": 78.971},
    {"symbol": "Se", "name": "Selenium", "atomic_number": 34, "atomic_weight": 78.971},
    {"symbol": "Br", "name": "Bromine", "atomic_number": 35, "atomic_weight": 83.889},
    {"symbol": "Kr", "name": "Krypton", "atomic_number": 36, "atomic_weight": 83.798},
    {"symbol": "Rb", "name": "Rubidium", "atomic_number": 37, "atomic_weight": 85.4678},
    {"symbol": "Sr", "name": "Strontium", "atomic_number": 38, "atomic_weight": 87.62},
    {"symbol": "Y", "name": "Yttrium", "atomic_number": 39, "atomic_weight": 88.905},
    {"symbol": "Zr", "name": "Zirconium", "atomic_number": 40, "atomic_weight": 91.224},
    {"symbol": "Nb", "name": "Niobrium", "atomic_number": 41, "atomic_weight":92.906},
    {"symbol": "Mo", "name": "Molybdenum", "atomic_number":42, "atomic_weight":95.95},
    {"symbol": "Tc", "name":"Technetium","atomic_number":43, "atomic_weight":98.905},
    {"symbol": "Ru", "name": "Ruthenium", "atomic_number":44, "atomic_weight":101.07},
    {"symbol": "Rh", "name": "Rhodium", "atomic_number":45, "atomic_weight":102.9058},
    {"symbol": "Pd", "name": "Palladium", "atomic_number":46, "atomic_weight":106.42},
    {"symbol": "Ag", "name": "Silver", "atomic_number":47, "atomic_weight":107.87},
    {"symbol": "Cd", "name": "Cadmium", "atomic_number":48, "atomic_weight":112.41},
    {"symbol": "In", "name": "Indium", "atomic_number":49, "atomic_weight":114.81},
    {"symbol": "Sn", "name": "Tin", "atomic_number":50, "atomic_weight":118.705},
    {"symbol": "Sb", "name": "Antimony", "atomic_number":51, "atomic_weight":121.765},
    {"symbol": "Te", "name": "Tellurium", "atomic_number":52, "atomic_weight":127.60},
    {"symbol": "I",  "name": "Iodine", "atomic_number":53, "atomic_weight":126.90},
]

# Remove the unused index 0

file_name = "elements.json"

# Write the data to the JSON file
with open(file_name, "w") as json_file:
    json.dump(elements, json_file, indent=1)

print(f"Data has been written to {file_name}.")
