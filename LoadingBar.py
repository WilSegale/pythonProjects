import time

def loading_bar(iteration, total, prefix='-', suffix='', length=30, fill='█'):
    percent = round(100 * (iteration / float(total)), 1)
    filled_length = round(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)

    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='', flush=False)

# Example usage:
total_items = 100
for i in range(total_items):
    # Perform some task here
    time.sleep(0.1)  # Simulating work

    # Update the loading bar
    loading_bar(i + 1, total_items, prefix='Progress:', suffix='Complete')

# Print a new line after the loading is complete
print("\nDone loading")