import matplotlib.pyplot as plt
import plotly.graph_objects as go
import shutil

# Bar graph data
total,used,free = shutil.disk_usage("/")
total // (2 ** 30)
free // (2 ** 30)
used // (2 ** 30)
labels = ['total','Used', 'Free']
values = [total,used,free]
fig = go.Figure(data=[go.Bar(x=labels, y=values, marker=dict(opacity=0.5))])
fig.show()
fig, ax = plt.subplots()

# Create bar graph
ax.bar(labels, values)

# Add shadow effect to bars
for patch in ax.patches:
    patch.set_alpha(0.5)