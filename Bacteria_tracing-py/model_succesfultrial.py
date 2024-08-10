import plotly.graph_objects as go
import numpy as np

# Sample data: 3D points (x, y, z)
x = np.random.rand(10)
y = np.random.rand(10)
z = np.sin(x) + np.cos(y)

points_array = np.load('H:\PERSONAL\PROJECTS\Programming\Bacteria_tracing-py\points.npy')

n_fragments = 11


# x1 = points_array[:, 0]
# y1 = points_array[:, 1]
# z1 = points_array[:, 2]


# scatter_trace = go.Scatter3d(
#     x=x1,
#     y=y1,
#     z=z1,
#     mode='markers',
#     marker=dict(
#         size=5,
#         color=z,          # Use color to represent z-values
#         colorscale='Viridis',  # Choose a colorscale
#         colorbar=dict(title='Z-Value'),
#     ),
# )

# # Create a surface mesh
# mesh1 = go.Mesh3d(x=x1, y=y1, z=z1, opacity=0.5)

# # Create a figure and add the mesh trace
# # fig = go.Figure(data=[mesh1, mesh2])
# fig = go.Figure(data=[mesh1])

for i in range(17):
    start = 2 + i * 36
    end = 2 + (i + 2) * 36
    
    mesh = go.Mesh3d(x=points_array[start:end, 0], y=points_array[start:end, 1], z=points_array[start:end, 2], opacity=0.5)
    if i == 0 :
        meshes = [mesh]
    else:
        meshes.append(mesh)
fig = go.Figure(data=meshes)


# Update layout to set the title and axis labels
fig.update_layout(
    title='Surface Mesh from 3D Points',
    scene=dict(
        xaxis_title='X-axis',
        yaxis_title='Y-axis',
        zaxis_title='Z-axis',
    )
)

# Show the plot
fig.show()
