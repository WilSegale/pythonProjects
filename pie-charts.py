import plotly.graph_objects as go
import shutil

total,used,free = shutil.disk_usage("/")
labels = ['Used', 'Free']
values = [used,free]
# Use `hole` to create a donut-like pie chart
fig = go.Figure(data = [go.Pie(labels=labels, values=values, hole=0.5)])
fig.show()