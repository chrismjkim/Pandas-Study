from PIL import Image
import cv2 as cv
from sklearn.cluster import KMeans
import numpy as np
from bisect import bisect_left, bisect_right

def mosaic(img, mos_n):
    
    for i in range(0, w, mos_n):
        for j in range(0, h, mos_n):
            # mosaic_pix: 묶어서 처리할 한 모자이크 단위
            # mosaic_pix = np.array(img.crop((i, j, i+n, j+n)))
            # cropped_img = cv2.getRectSubPix(img, size, center)
            mosaic_pix = rgbs[j:j+mos_n, i:i+mos_n, :]

            r = np.mean(mosaic_pix[:, :, 0])
            g = np.mean(mosaic_pix[:, :, 1])
            b = np.mean(mosaic_pix[:, :, 2])

            for x in range(i, min(i+mos_n, w)):
                for y in range(j, min(j+mos_n, h)):
                    rgbs[y][x][0] = r
                    rgbs[y][x][1] = g
                    rgbs[y][x][2] = b

    # Convert NumPy array to PIL Image instance
    img = Image.fromarray(np.uint8(rgbs))
    img.save("images/mosaic.jpg")

def bit_art(img, mos_n, col_n):
    
    colset = [round(255*x/col_n) for x in range(col_n+1)] 
   
    for i in range(0, w, mos_n):
        for j in range(0, h, mos_n):
            # mosaic_pix: 묶어서 처리할 한 모자이크 단위
            mosaic_pix = rgbs[j:j+mos_n, i:i+mos_n, :]
            
            r = np.mean(mosaic_pix[:, :, 0])
            g = np.mean(mosaic_pix[:, :, 1])
            b = np.mean(mosaic_pix[:, :, 2])
                
            if r not in colset:
                if r- bisect_left(colset, r) < bisect_right(colset, r)-r:
                    r = colset[bisect_left(colset, r)]
                else:
                    r = colset[bisect_right(colset, r)]

            if g not in colset:
                if g- bisect_left(colset, g) < bisect_right(colset, g)-g:
                    g = colset[bisect_left(colset, g)]
                else:
                    g = colset[bisect_right(colset, g)]

            if b not in colset:
                if b- bisect_left(colset, b) < bisect_right(colset, b)-b:
                    b = colset[bisect_left(colset, b)]
                else:
                    b = colset[bisect_right(colset, b)]

            for x in range(i, min(i+mos_n, w)):
                for y in range(j, min(j+mos_n, h)):
                    rgbs[y][x][0] = r
                    rgbs[y][x][1] = g
                    rgbs[y][x][2] = b

    img = Image.fromarray(np.uint8(rgbs))
    img.save("images/bit_art.jpg")

def color_quantization(img, col_n):
    
    colset = [round(255*x/col_n) for x in range(col_n+1)] 
   
    for i in range(w):
        for j in range(h):

            r = rgbs[j][i][0]
            g = rgbs[j][i][1]
            b = rgbs[j][i][2]

            if r not in colset:
                if r- bisect_left(colset, r) < bisect_right(colset, r)-r:
                    r = colset[bisect_left(colset, r)]
                else:
                    r = colset[bisect_right(colset, r)]

            if g not in colset:
                if g- bisect_left(colset, g) < bisect_right(colset, g)-g:
                    g = colset[bisect_left(colset, g)]
                else:
                    g = colset[bisect_right(colset, g)]

            if b not in colset:
                if b- bisect_left(colset, b) < bisect_right(colset, b)-b:
                    b = colset[bisect_left(colset, b)]
                else:
                    b = colset[bisect_right(colset, b)]

            rgbs[j][i][0] = r
            rgbs[j][i][1] = g
            rgbs[j][i][2] = b

    img = Image.fromarray(np.uint8(rgbs))
    img.save("images/color_quantization.jpg")

def grayscale(img):
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imwrite("images/grayscale.jpg", img)

def color_scale(img, filter_color):
    if filter_color=='red':
        rgbs[:, :, 1]=0
        rgbs[:, :, 2]=0
        img = Image.fromarray(np.uint8(rgbs))
        img.save("images/red_scale.jpg")

    elif filter_color=='green':
        rgbs[:][:][0]=rgbs[:][:][2]=0
        img = Image.fromarray(np.uint8(rgbs))
        img.save("images/green_scale.jpg")

    elif filter_color=='blue':
        rgbs[:][:][0]=rgbs[:][:][1]=0
        img = Image.fromarray(np.uint8(rgbs))
        img.save("images/blue_scale.jpg")

def color_cluster(col_n):
    rgbs_flat = rgbs.reshape((-1, 3))
    kmeans = KMeans(n_clusters=col_n)
    kmeans.fit(rgbs_flat)
    labels = kmeans.labels_

    rgbs_cl = kmeans.cluster_centers_[labels]
    rgbs_cl = np.uint8(rgbs_cl.reshape((h, w, c)))

    img_clustered = Image.fromarray(rgbs_cl)
    img_clustered.save("images/color_cluster.jpg")
    

"""이 위로는 이미지 처리 함수, 이 아래로는 parameter 입력 및 코드 입력"""

# 편집할 이미지
img = cv.imread("star.jpg")
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
rgbs = np.array(img)

# c: channels -> 색상 채널, 즉 R, G, B의 3가지인 '3' 저장되어 있음
h, w, c = rgbs.shape


# parameters to change
mos_n = 5
col_n = 10
filter_color='red' # red, green, blue 중 선택

"""
mosaic(img, mos_n)
bit_art(img, mos_n, col_n)
color_quantization(img, col_n)
grayscale(img)
color_scale(img, filter_color)
color_cluster(img, col_n)
"""