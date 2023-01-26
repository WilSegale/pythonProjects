import pandas as pd
import shutil
total, used, free = shutil.disk_usage("/")


# Data for the CSV chart
data = {'Total': [total // (2 ** 30)],
        'Free': [free // (2 ** 30)],
        'Used': [used // (2 ** 30)]}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Output the DataFrame to a CSV file
df.to_csv('DiskSpace.csv', index=False)
