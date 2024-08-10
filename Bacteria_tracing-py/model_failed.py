import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# Replace 'images_list' with your list of 2D images (each image is a 2D NumPy array)
base_dir = "H:\PERSONAL\PROJECTS\Programming\Bacteria_tracing-py\encapsulation_04001_Series004_z"

images_namelist = [f"{base_dir}\encapsulation_04001_Series004_z{i:03d}.tif" for i in range(0, 198)]
# print(images_namelist)

# image = plt.imread(images_namelist[0]).transpose()[0]

images_list = [plt.imread(image).transpose()[0] for image in images_namelist]
# print(images_list)
# Convert the list of images into a 3D NumPy array
stacked_images = np.array(images_list)
print(stacked_images.shape)

# Convert the list of images into a 3D NumPy array
stacked_images = np.array(images_list)

# np.save("stacked_images.npy", stacked_images)

# Create a 3D figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Get the dimensions of the stacked images
depth, height, width = stacked_images.shape

# Create 3D coordinates for the voxel grid
x, y, z = np.meshgrid(np.arange(width), np.arange(height), np.arange(depth))

# Flatten the 3D coordinates and the stacked images for plotting
x = x.flatten()
y = y.flatten()
z = z.flatten()
colors = stacked_images.flatten()

# Plot the 3D volume with varying colors
ax.scatter(x, y, z, c=colors, cmap='viridis', s=1)

# Set axis labels (you can customize these as needed)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set the aspect ratio to be equal for all axes
ax.set_aspect('auto')

# Show the 3D plot
plt.show()
