from DontEdit import *

def convert_kb_to_other_units(kb):
    mb = kb / 1024
    gb = kb / (1024 ** 2)
    tb = kb / (1024 ** 3)
    pb = kb / (1024 ** 4)
    eb = kb / (1024 ** 5)
    zb = kb / (1024 ** 6)
    yb = kb / (1024 ** 7)
    return mb, gb, tb, pb, eb, zb, yb

# Get user input
kb_value = float(input("Enter the number of kilobytes (KB): "))

# Convert KB to MB, GB, and TB
mb_value, gb_value, tb_value, pb_value, eb_value, zb_value, yb_value= convert_kb_to_other_units(kb_value)

# Print the results
print(f"{kb_value:,.2f} {GREEN}KB{RESET} is:")
print(f"{mb_value:,.2f} {GREEN}MB{RESET}")
print(f"{gb_value:,.2f} {GREEN}GB{RESET}")
print(f"{tb_value:,.2f} {GREEN}TB{RESET}")
print(f"{pb_value:,.2f} {GREEN}PB{RESET}")
print(f"{eb_value:,.2f} {GREEN}EB{RESET}")
print(f"{zb_value:,.2f} {GREEN}ZB{RESET}")
print(f"{yb_value:,.2f} {GREEN}YB{RESET}")
