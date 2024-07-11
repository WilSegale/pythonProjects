from DontEdit import *

def convert_kb_to_other_units(kb):
    mb = kb / 1024
    gb = kb / (1024 * 1024)
    tb = kb / (1024 * 1024 * 1024)
    return mb, gb, tb

# Get user input
kb_value = float(input("Enter the number of kilobytes (KB): "))

# Convert KB to MB, GB, and TB
mb_value, gb_value, tb_value = convert_kb_to_other_units(kb_value)

# Print the results
print(f"{kb_value:,.2f} {GREEN}KB{RESET} is:")
print(f"{mb_value:,.2f} {GREEN}MB{RESET}")
print(f"{gb_value:,.2f} {GREEN}GB{RESET}")
print(f"{tb_value:,.2f} {GREEN}TB{RESET}")
