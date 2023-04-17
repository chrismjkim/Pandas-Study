import random
import numpy as np
from bisect import bisect_left, bisect_right
import cv2 as cv
from PIL import Image

def distance(p1, p2):
    return round((p1[0]-p2[0])**2+(p1[1]-p2[1])**2+(p1[2]-p2[2])**2, 1)

def error_size(prev, calib):
    error_sum = sum(abs(prev[i]-calib[i]) for i in range(k))
    return sum(error_sum)



img = cv.imread('star.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
h, w, c = img.shape
pixels = img.reshape(-1, 3).tolist()
print(pixels)
k = 5
p_value = k * 1

calib_means = sorted(random.sample(pixels, k))
print("these are the initial random means:", calib_means)
actual_means = list(calib_means)
print(f'actual means: {actual_means}')
prev_means = []

while True: # 선 반복 후 조건문

    clusters = [[] for _ in range(k)] # 군집 초기화
    prev_means=np.copy(calib_means) # 이전 단계 군집중심 값

    # 각 픽셀에 대해 각 군집중심까지의 거리들을 계산함
    for i in pixels:
        dists = [[] for _ in range(2)]
        for m  in calib_means: # m = [int, int, int]
            dists[0].append(m)
            dists[1].append(distance(i, m))
        # centroid에는 각 픽셀에서 가장 가까운 군집중심의 index를 저장함
        centroid = dists[1].index(min(dists[1]))
        # 해당하는 군집에 픽셀을 저장함
        clusters[centroid].append(tuple(i))

    # 각 군집의 군집중심을 계산함
    for x in range(k):
        clust = np.array(clusters[x])
        actual_means[x] = (np.mean(clust[:,0]), np.mean(clust[:,1]), np.mean(clust[:,2]))

    # 각 군집중심에서 가장 가까운 픽셀의 RGB값을 저장함
    for x in range(k):
        # find closest element of 'list' from 'float_means[x]' and append to means[x]
        # it just integeifies the 'actual_means' yet
        calib_means[x] = (round(actual_means[x][0]), round(actual_means[x][1]), round(actual_means[x][2]))

    # 오차의 총합이 세팅한 수준보다 작으면 while문을 종료함

    print(f'prev_means:\n{prev_means}')
    print(f'calib_means:\n{calib_means}')
    print(f'error size: {error_size(prev_means, calib_means)}')
    if error_size(prev_means, calib_means) <= p_value:
        break

print(f'FINISHED\n군집: {clusters} \n이전 군집중심: {prev_means}\n무게중심 좌표: {actual_means}\n새 군집중심: {calib_means}')
# ----------------------------------------------------------------------------------------------------------------------------

"""
    for i in pixels:
        # find closest mean of 'i' from 'calibrated_means' and append ''i' into 'clusters'
        dists = [[] for _ in range(2)]
        for m in calib_means:
            dists[0].append(m)
            dists[1].append((distance(i, m)))

        print("this is the distance list to each mean from pixel:", dists)

        centroid = dists[1].index(min(dists[1]))
        clusters[centroid].append(i)
    print("clusters:", clusters)
    # calculate_clusters_mean
    for x in range(k):
        clust = np.array(clusters[x])
        actual_means[x] = (np.mean(clust[:,0]), np.mean(clust[:,1]), np.mean(clust[:,2]))
    # update means

-----------------------------------------------------------------------
    for x in range(k):
        # find closest element of 'list' from 'float_means[x]' and append to means[x]
        # it just integeifies the 'actual_means' yet
        calib_means[x] = (round(actual_means[x][0]), round(actual_means[x][1]), round(actual_means[x][2]))

# (while ends here)
        
print(f'FINISHED\n군집: {clusters} \n이전 군집중심: {prev_means}\n무게중심 좌표: {actual_means}\n새 군집중심: {calib_means}')

for pixel in pixels:
    pixel = calibrated_means(clusters.index(pixel)[0])

img = Image.fromarray(np.uint8(pixels))
img.save("images/kmeans.jpg")"""
