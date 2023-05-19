import pandas as pd
import shutil
from colorama import *

GREEN = Fore.GREEN
RED = Fore.RED
YELLOW = Fore.YELLOW

total, used, free = shutil.disk_usage("/")

# Data for the CSV chart
data = {'Total': [total // (2 ** 30)],
        'Free':  [free // (2 ** 30)],
        'Used':  [used // (2 ** 30)]}

# Create a DataFrame from the data
df = pd.DataFrame(data)
# Output the DataFrame to a CSV file
df.to_csv('DiskSpace.csv', index=False)
print(GREEN +"Total: %d GB " % (total // (2 ** 30)))
print(RED +"Used: %d GB " % (used // (2 ** 30)))
print(YELLOW +"Free: %d GB " % (free // (2 ** 30))+ Fore.RESET)