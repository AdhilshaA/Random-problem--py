# from mpl_toolkits.mplot3d import Axes3D
# import matplotlib.pyplot as plt
# from matplotlib import cm
# from matplotlib.ticker import LinearLocator, FormatStrFormatter
# import numpy as np


# fig = plt.figure()
# ax = fig.gca(projection='3d')

# # Make data.
# X = np.arange(-5, 5, 0.25)
# Y = np.arange(-5, 5, 0.25)
# print(X,'\n',Y)
# X, Y = np.meshgrid(X, Y)
# print(X,'\n',Y)

# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)
# print(Z)
# # # Plot the surface.
# surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
#                        linewidth=0, antialiased=False)

# # Customize the z axis.
# ax.set_zlim(-1.01, 1.01)
# ax.zaxis.set_major_locator(LinearLocator(10))
# ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# # Add a color bar which maps values to colors.
# fig.colorbar(surf, shrink=0.5, aspect=5)

# plt.show()

# from mpl_toolkits.mplot3d import Axes3D
# import matplotlib.pyplot as plt
# import numpy as np


# n_radii = 8
# n_angles = 36

# # Make radii and angles spaces (radius r=0 omitted to eliminate duplication).
# radii = np.linspace(0.125, 1.0, n_radii)
# angles = np.linspace(0, 2*np.pi, n_angles, endpoint=False)

# # Repeat all angles for each radius.
# angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)

# # Convert polar (radii, angles) coords to cartesian (x, y) coords.
# # (0, 0) is manually added at this stage,  so there will be no duplicate
# # points in the (x, y) plane.
# x = np.append(0, (radii*np.cos(angles)).flatten())
# y = np.append(0, (radii*np.sin(angles)).flatten())

# # Compute z to make the pringle surface.
# z = np.sin(-x*y)
# print(x,y,z)

# fig = plt.figure()
# ax = fig.gca(projection='3d')

# ax.plot_trisurf(x, y, z, linewidth=0.2, antialiased=True)

# plt.show()



import numpy as np
from mayavi import mlab
import matplotlib.pyplot as plt

X = np.array([0, 1, 0, 1, 0.75])
Y = np.array([0, 0, 1, 1, 0.75])
Z = np.array([1, 1, 1, 1, 2])

data = np.array([[-0.807237702464, 0.904373229492, 111.428744443],
[-0.802470821517, 0.832159465335, 98.572957317],
[-0.801052795982, 0.744231916692, 86.485869328],
[-0.802505546206, 0.642324228721, 75.279804677],
[-0.804158144115, 0.52882485495, 65.112895758],
[-0.806418040943, 0.405733109371, 56.1627277595],
[-0.808515314192, 0.275100227689, 48.508994388],
[-0.809879521648, 0.139140394575, 42.1027499025],
[-0.810645106092, -7.48279012695e-06, 36.8668106345],
[-0.810676720161, -0.139773175337, 32.714580273],
[-0.811308686707, -0.277276065449, 29.5977405865],
[-0.812331692291, -0.40975978382, 27.6210856615],
[-0.816075037319, -0.535615685086, 27.2420699235],
[-0.823691366944, -0.654350489595, 29.1823292975],
[-0.836688691603, -0.765630198427, 34.2275056775],
[-0.854984518665, -0.86845932028, 43.029581434],
[-0.879261949054, -0.961799684483, 55.9594146815],
[-0.740499820944, 0.901631050387, 97.0261463995],
[-0.735011699497, 0.82881933383, 84.971061395],
[-0.733021568161, 0.740454485354, 73.733621269],
[-0.732821755233, 0.638770044767, 63.3815970475],
[-0.733876941678, 0.525818698874, 54.0655910105],
[-0.735055978521, 0.403303715698, 45.90859502],
[-0.736448900325, 0.273425879041, 38.935709456],
[-0.737556181137, 0.13826504904, 33.096106049],
[-0.738278724065, -9.73058423274e-06, 28.359664343],
[-0.738507612286, -0.138781586244, 24.627237837],
[-0.738539663773, -0.275090412979, 21.857410904],
[-0.739099040189, -0.406068448513, 20.1110519655],
[-0.741152200369, -0.529726022182, 19.7019157715]])

data = np.transpose(data)
X = data[0]
Y=data[1]
Z=data[2]
# Define the points in 3D space
# including color code based on Z coordinate.
pts = mlab.points3d(X, Y, Z, Z)
# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
# ax.scatter(X,Y,Z)
# plt.show()
# Triangulate based on X, Y with Delaunay 2D algorithm.
# Save resulting triangulation.
mesh = mlab.pipeline.delaunay2d(pts)

# Remove the point representation from the plot
pts.remove()

# Draw a surface based on the triangulation
surf = mlab.pipeline.surface(mesh)
surf.actor.actor.scale = (100.0, 50.0, 1.0)
# Simple plot.
# mlab.set_xlim()
# mlab.set_ylim()
# mlab.set_zlim()
mlab.axes(extent=[0.73,0.83,-1,1,20,112])
mlab.xlabel("x")
mlab.ylabel("y")
mlab.zlabel("z")
mlab.show()
