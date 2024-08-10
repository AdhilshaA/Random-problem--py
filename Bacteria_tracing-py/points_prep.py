import mylibrary_general as mylib
import numpy as np
import math as m

ran = mylib.randgen(21, interval=(0, m.pi), decimals = 4)
radius = 5
theta = ran.gen()
phi = 2*ran.gen()
points = np.array([(radius*m.sin(theta)*m.cos(phi), radius * m.sin(theta)*m.sin(phi), radius * m.cos(theta))])


# for i in range(1000):
#     theta = ran.gen()
#     phi = ran.gen()

points = np.array([(0,0,radius),(0,0,-radius)])

for theta in range(5,180,10):
    for phi in range(0,360,10):
        points = np.append(points, [(radius*m.sin(theta*m.pi/180)*m.cos(phi*m.pi/180), radius * m.sin(theta*m.pi/180)*m.sin(phi*m.pi/180), radius * m.cos(theta*m.pi/180))], axis=0)


np.save('points.npy', points)