import matplotlib.pyplot as plt
import pandas as pd

# Read and process data
data = pd.read_csv('disk_space_data.csv')
data['timestamp'] = pd.to_datetime(data['timestamp'])

# Create the line graph
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed

plt.plot(data['timestamp'], data['disk_space'], marker='o', linestyle='-', color='b')

plt.title('Disk Space Usage Over Time')
plt.xlabel('Timestamp')
plt.ylabel('Disk Space (GB)')

plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.grid(True)

plt.tight_layout()

plt.show()

