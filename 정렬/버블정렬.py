
def bubbleSort(x):
    length = len(x)-1
    for i in range(length):
        for j in range(length-i):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]
    return x


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


arr = [9, 2, 5, 3, 6, 4, 8, 1, 7]


for front_index in range(0, len(arr) - 1):
    for index in range(front_index + 1, len(arr)):
        if arr[front_index] > arr[index]:
            arr[front_index], arr[index] = arr[index], arr[front_index]
print(bubbleSort(arr))
