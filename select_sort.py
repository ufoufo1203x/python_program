data = [100, 90, 50, 40, 30]

for i in range(1, len(data)):
    j = i
    while (j > 0) and (data[j-1] > data[j]):
        tmp = data[j-1]
        data[j-1] = data[j]
        data[j] = tmp
        j -= 1
        
print(data)