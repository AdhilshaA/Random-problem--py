import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from scipy.spatial import Delaunay

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

points_array = np.load('Bacteria tracing -py\points.npy')

tri = Delaunay(points_array)

# Plot the 3D points
ax.scatter(points_array[:, 0], points_array[:, 1], points_array[:, 2], c='b', marker='o',s = 1)

# Plot the triangulated surfaces
for simplex in tri.simplices:
    vertices = points_array[simplex]
    poly3d = [[vertices[j] for j in range(3)]]
    ax.add_collection3d(Poly3DCollection(poly3d, facecolors='cyan', linewidths=0, edgecolors='r', alpha=0.5))

plt.show()