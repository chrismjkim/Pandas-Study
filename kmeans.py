import random
import numpy as np
from bisect import bisect_left, bisect_right

pixels = [1, 4, 2, 8, 5 ,7, 12, 3, 5, 2, 3 ,5]
k = 3

calibrated_means = sorted(random.sample(pixels, k))
print(calibrated_means)
actual_means = list(calibrated_means)
prev_means = []

while prev_means!=calibrated_means:
    clusters = [[] for _ in range(k)]
    prev_means=list(calibrated_means)
    for i in pixels:
        # find closest mean of 'i' from 'means' and append into 'clusters'  
        index = bisect_left(calibrated_means, i)
        if index==0:
            clusters[0].append(i)
        elif index==k:
            clusters[-1].append(i)
        else:
            if i-calibrated_means[index-1] < calibrated_means[index]-i:
                clusters[index-1].append(i)
            else:
                clusters[index].append(i)
    # calculate_clusters_mean
    for x in range(k):
        actual_means[x] = np.mean(clusters[x])
    # update means: find closest element of 'list' from 'float_means[x]' and append to means[x]
    for x in range(k):
        calibrated_means[x] = round(actual_means[x])

print(f'clusters: {clusters} \nprev_means: {prev_means}\nmeans: {actual_means}\nnew pivots: {calibrated_means}')
