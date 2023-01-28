import matplotlib.pyplot as plt
import plotly.graph_objects as go


# Bar graph data
labels = ['A', 'B', 'C', 'D']
values = [1, 4, 2, 5]
fig = go.Figure(data=[go.Bar(x=labels, y=values, marker=dict(opacity=0.5))])
fig.show()
fig, ax = plt.subplots()

# Create bar graph
ax.bar(labels, values)

# Add shadow effect to bars
for patch in ax.patches:
    patch.set_alpha(0.5)

plt.show()
