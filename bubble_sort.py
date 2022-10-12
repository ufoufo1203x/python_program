def bubble_sort(data):
    for i in range(1,len(data)):
        for j in range(0, len(data)-i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                
if __name__ == '__name__':
    data = [5,4,3,2,-1]
    bubble_sort(data)
    print(data) 