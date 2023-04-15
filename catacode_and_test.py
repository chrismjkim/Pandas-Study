import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

col_n = int(input())
colset = [round(255*x/col_n) for x in range(col_n+1)] 

print(colset)

r, g, b = map(int, input().split())
        
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
        b = bisect_left(colset, b)
    else:
        b = bisect_right(colset, b)

print(r, g, b)