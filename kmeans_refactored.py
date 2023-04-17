import random
import numpy as np
import cv2 as cv
from PIL import Image

def distance(p1, p2):
    return round((p1[0]-p2[0])**2+(p1[1]-p2[1])**2+(p1[2]-p2[2])**2, 1)

def error_size(previous, current):
    previous = np.array(previous)
    current = np.array(current)
    error_sum = sum(abs(previous[i]-current[i]) for i in range(k))
    return sum(error_sum)

img = cv.imread('shin.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
h, w, c = img.shape
pixels = img.reshape(-1, 3).tolist()

k = 8
p_value = (k*(k-1))//2

cl_centers = sorted(random.sample(pixels, k))
prev_cl_centers = []

while True: # 선 반복 후 조건문
    clusters = [[(0,0,0), (0,0,0), 0] for _ in range(k)] # 군집 초기화 및 정의 ([군집중심 좌표, 원소 총합, 원소 개수]*군집 개수)
    labels = [(0,0,0)]*(h*w) # 라벨 초기화 및 정의([군집중심 좌표]*픽셀 수)

    prev_cl_centers=tuple(cl_centers) # 이전 단계 군집중심 값
    # 군집중심들을 배열에 우선 배치해둠
    for i in range(k):
        clusters[i][0] = cl_centers[i] 

    labeling_cnt = 0
    # 각 픽셀에 대해 각 군집중심까지의 거리들을 계산함
    for i in pixels:
        # 한 픽셀에서 군집중심까지의 거리들을 계산함
        dists = []
        for center in cl_centers: # center = [int, int, int]
            dists.append(distance(i, center))

        # centroid에는 각 픽셀에서 가장 가까운 군집중심의 index를 저장함
        centroid = dists.index(min(dists))

        # 해당하는 군집에 픽셀을 저장함
        clusters[centroid][1] = tuple(x + y for x, y in zip(clusters[centroid][1], i))
        clusters[centroid][2] += 1

        # 해당 픽셀을 라벨링함
        labels[labeling_cnt] = cl_centers[centroid]
        labeling_cnt += 1
    print(f'cluster infos: {clusters}')

    # 각 군집의 군집중심을 계산함
    for x in range(k):
        cl_centers[x] = tuple(round(sum/clusters[x][2]) for sum in clusters[x][1])

    # 오차의 총합이 세팅한 수준보다 작으면 while문을 종료함
    print(f'previous cluster centers:\n{prev_cl_centers}')
    print(f'cluster centers:\n{cl_centers}')
    print(f'error size: {error_size(prev_cl_centers, cl_centers)}')
    if error_size(prev_cl_centers, cl_centers) <= p_value:
        break

print(f'FINISHED\n최종 군집중심: {cl_centers}')
print(f'변환해야 하는 rgb값 배열: {labels}')

labels = np.array(labels).reshape(h, w, c)
print(labels)

img = Image.fromarray(np.uint8(labels))
img.save("images/짱구_cartooned.jpg")

