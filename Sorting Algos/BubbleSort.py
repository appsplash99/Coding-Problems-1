def bubble_sort(data):
    swap=False
    for i in range(len(data)-1):
        for j in range(len(data)-1-i):
            if data[j] > data [j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                swap=True
            if not(swap):
                return "Already sorted"
    return data

print(bubble_sort([1,2,4,5,6]))