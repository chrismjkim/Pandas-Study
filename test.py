list = [1,2,3,4,5]

sum = 0
for x in list:
    sum += x
avg = sum/len(list)

list[0] = avg
print(list[0])