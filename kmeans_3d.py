import random
import numpy as np
from bisect import bisect_left, bisect_right
import cv2 as cv
from PIL import Image

def distance(p1, p2):
    return round((p1[0]-p2[0])**2+(p1[1]-p2[1])**2+(p1[2]-p2[2])**2, 1)

"""
img = cv.imread('star.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)"""

pixels = [(255,0,0), (240,64,72), (34,177,76), 
          (181,230,29), (63,72,204), (112,146,190), 
          (163,73,164), (255,127,39), (0,0,0),
          (49,49,49), (25,25,25)]
"""pixels = np.array(img)"""
k = 4

calibrated_means = sorted(random.sample(pixels, k))
print("these are the initial random means:", calibrated_means)
actual_means = list(calibrated_means)
prev_means = []

while prev_means!=calibrated_means:
    clusters = [[] for _ in range(k)]
    prev_means=list(calibrated_means)
    for i in pixels:
        # find closest mean of 'i' from 'calibrated_means' and append ''i' into 'clusters'
        dist_list = [[] for _ in range(2)]
        for m in calibrated_means:
            dist_list[0].append(m)
            dist_list[1].append((distance(i, m)))

        print("this is the distance list to each mean from pixel:", dist_list)

        centroid = dist_list[1].index(min(dist_list[1]))
        clusters[centroid].append(i)
    print("clusters:", clusters)
    # calculate_clusters_mean
    for x in range(k):
        clust = np.array(clusters[x])
        actual_means[x] = (np.mean(clust[:,0]), np.mean(clust[:,1]), np.mean(clust[:,2]))
    # update means

    for x in range(k):
        # find closest element of 'list' from 'float_means[x]' and append to means[x]
        calibrated_means[x] = (round(actual_means[x][0]), round(actual_means[x][1]), round(actual_means[x][2]))

print(f'FINISHED\n집단: {clusters} \n이전 집단중심: {prev_means}\n무게중심 좌표: {actual_means}\n새 집단중심: {calibrated_means}')

"""for pixel in pixels:
    pixel = calibrated_means(clusters.index(pixel)[0])

img = Image.fromarray(np.uint8(pixels))
img.save("images/kmeans.jpg")"""