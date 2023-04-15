import numpy as np

# define the coordinates of the two points
point1 = (3, 3, 3)
point2 = (6, 7, 5)

# convert the points to numpy arrays
p1 = np.array(point1)
p2 = np.array(point2)

# calculate the distance between the two points
distance = np.linalg.norm(p2-p1)

# print the distance
print(distance)