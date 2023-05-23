import matplotlib.pyplot as plt

# Sample data
categories = ['Category A', 'Category B', 'Category C']
values = [10, 20, 15]

# Create bar graph
plt.bar(categories, values)

# Add numbers on top of each bar
for i, value in enumerate(values):
    plt.text(i, value + 1, str(value), ha='center')

# Display the graph
plt.show()
