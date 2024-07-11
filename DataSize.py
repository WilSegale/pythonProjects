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
print(f"{kb_value} KB is:")
print(f"{mb_value:.4f} MB")
print(f"{gb_value:.4f} GB")
print(f"{tb_value:.10f} TB")
