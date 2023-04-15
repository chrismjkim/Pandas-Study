import random
import numpy as np
from bisect import bisect_left, bisect_right

def avg(list):
    sum = 0 
    for i in list:
        sum += i
    return round(sum/len(list), 1)


pixels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
k = 4

means = sorted(random.sample(pixels, k))
print(means)
float_means = list(means)
prev_means = []

while prev_means!=means:
    clusters = [[] for _ in range(k)]
    prev_means=list(means)
    for i in pixels:
        # find closest mean of 'i' from 'means' and append into 'clusters'
        index = bisect_left(means, i)
        if index==0:
            clusters[0].append(i)
        elif index==k:
            clusters[-1].append(i)
        else:
            if i-means[index-1] < means[index]-i:
                clusters[index-1].append(i)
            else:
                clusters[index].append(i)
    # calculate_clusters_mean
    for x in range(k):
        float_means[x] = np.mean(clusters[x])
    # update means

    for x in range(k):
        # find closest element of 'list' from 'float_means[x]' and append to means[x]
        means[x] = round(float_means[x])

print(f'clusters: {clusters} \nprev_means: {prev_means}\nmeans: {float_means}\nnew pivots: {means}')
