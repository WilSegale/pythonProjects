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
    {"symbol": "Y",  "name": "Yttrium", "atomic_number": 39, "atomic_weight": 88.905},
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
    {"symbol": "Xe", "name": "Xenon", "atomic_number":54, "atomic_weight":131.29},
    {"symbol": "Cs", "name": "Caesium", "atomic_number":55, "atomic_weight":132.91},
    {"symbol": "Ba", "name": "Barium", "atomic_number":56, "atomic_weight":137.32},
    {"symbol": "La", "name": "Lanthanum", "atomic_number":57,"atomic_weight":138.905},
    {"symbol": "Ce", "name": "Cerium", "atomic_number":58, "atomic_weight":140.12},
    {"symbol": "Pr", "name": "Praseodymium","atomic_number":59, "atomic_weight":140.905},
    {"symbol": "Nd", "name": "Neodymium", "atomic_number":60, "atomic_weight":144.24},
    {"symbol": "Pm", "name": "Promethium", "atomic_number":61, "atomic_weight":145.96},
    {"symbol": "Sm", "name": "Samarium", "atomic_number":62, "atomic_weight":150.39},
    {"symbol": "Eu", "name": "Europium", "atomic_number":63, "atomic_weight":151.96},
    {"symbol": "Gd", "name": "Gadolinium", "atomic_number":64, "atomic_weight":157.25},
    {"symbol": "Tb", "name": "Terbium", "atomic_number":65, "atomic_weight":158.921},
    {"symbol": "Dy", "name": "Dysprosium", "atomic_number":66, "atomic_weight":162.50},
    {"symbol": "Ho", "name": "Holmium", "atomic_number":67, "atomic_weight":164.938},
    {"symbol": "Er", "name": "Erbium", "atomic_number":68, "atomic_weight":167.26},
    {"symbol": "Tm", "name": "Thulium", "atomic_number":69, "atomic_weight":168.934},
    {"symbol": "Yb", "name": "Ytterbium", "atomic_number":70, "atomic_weight":173.05},
    {"symbol": "Lu", "name": "Lutetium", "atomic_number":71, "atomic_weight":174.966},
    {"symbol": "Hf", "name": "Hafnium", "atomic_number":72, "atomic_weight":178.49},
    {"symbol": "Ta", "name": "Tantalum", "atomic_number":73, "atomic_weight":180.94},
    {"symbol": "W",  "name": "Tungsten", "atomic_number":74, "atomic_weight":183.84},
    {"symbol": "Re", "name": "Rhenium", "atomic_number":75, "atomic_weight":186.204},
    {"symbol": "Os", "name": "Osmium", "atomic_number":76, "atomic_weight":190.23},
    {"symbol": "Ir", "name": "Iridium", "atomic_number":77, "atomic_weight":192.21},
    {"symbol": "Pt", "name": "Protactinium", "atomic_number":78, "atomic_weight":195.084},
    {"symbol": "Au", "name": "Neptunium", "atomic_number":79, "atomic_weight":196.966},
    {"symbol": "Hg", "name": "Hydrogen", "atomic_number":80, "atomic_weight":200.59},
    {"symbol": "Tl", "name": "Thallium", "atomic_number":81, "atomic_weight":204.384},
    {"symbol": "Pb", "name": "Lead", "atomic_number":82, "atomic_weight":207.2},
    {"symbol": "Bi", "name": "Bismuth", "atomic_number":83, "atomic_weight":208.98},
    {"symbol": "Po", "name": "Polonium", "atomic_number":84, "atomic_weight":212.42},
    {"symbol": "At", "name": "Astatine", "atomic_number":85, "atomic_weight":210.96},
    {"symbol": "Rn", "name": "Radon", "atomic_number":86, "atomic_weight":222},
    {"symbol": "Fr", "name": "Francium", "atomic_number":87, "atomic_weight":226.2},
    {"symbol": "Ra", "name": "Actinium", "atomic_number":88, "atomic_weight":230.2},
    {"symbol": "Ac", "name": "Astatine", "atomic_number":89, "atomic_weight":231.09},
    {"symbol": "Th", "name": "Thallium", "atomic_number":90, "atomic_weight":232.08},
    {"symbol": "Pa", "name": "Platinum", "atomic_number":91, "atomic_weight":238.04},
    {"symbol": "U", "name": "Uranium", "atomic_number":92, "atomic_weight":239},
    {"symbol": "Np", "name": "Neptunium", "atomic_number":93, "atomic_weight":240.02},
    {"symbol": "Pu", "name": "Plutonium", "atomic_number":94, "atomic_weight":244.03},
    {"symbol": "Am", "name": "Americium", "atomic_number":95, "atomic_weight":243.05},
    {"symbol": "Cm", "name": "Cermium", "atomic_number":96, "atomic_weight":247.04},
    {"symbol": "Bk", "name": "Berkelium", "atomic_number":97, "atomic_weight":251.02},
    {"symbol": "Cf", "name": "Californium", "atomic_number":98, "atomic_weight":252.06},
    {"symbol": "Es", "name": "Einsteinium", "atomic_number":99, "atomic_weight":252.05},
    {"symbol": "Fm", "name": "Flerovium", "atomic_number":100, "atomic_weight":257.05},
    {"symbol": "Md", "name": "Mendelevium", "atomic_number":101, "atomic_weight":258},
    {"symbol": "No", "name": "Neodymium", "atomic_number":102, "atomic_weight":259},
    {"symbol": "Lr", "name": "Livermorium", "atomic_number":103, "atomic_weight":266},
    {"symbol": "Rf", "name": "Roentgenium", "atomic_number":104, "atomic_weight":267},
    {"symbol": "Db", "name": "Deuteron", "atomic_number":105, "atomic_weight":268},
    {"symbol": "Sg", "name": "Seaborgium", "atomic_number":106, "atomic_weight":269},
    {"symbol": "Bh", "name": "Bohrium", "atomic_number":107, "atomic_weight":270},
    {"symbol": "Hs", "name": "Hassium", "atomic_number":108, "atomic_weight":277},
    {"symbol": "Mt", "name": "Meitnerium", "atomic_number":109, "atomic_weight":278},
    {"symbol": "Ds", "name": "Darmstadtium", "atomic_number":110, "atomic_weight":281},
    {"symbol": "Rg", "name": "Rutherfordium", "atomic_number":111, "atomic_weight":282},
    {"symbol": "Cn", "name": "Copernicium", "atomic_number":112, "atomic_weight":285},
    
]

# Remove the unused index 0

file_name = "elements.json"

# Write the data to the JSON file
with open(file_name, "w") as json_file:
    json.dump(elements, json_file, indent=0)

print(f"Data has been written to {file_name}.")
