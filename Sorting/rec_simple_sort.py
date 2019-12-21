# Recursively finds the biggest index, pops it to answer until array is empty #

arr = [1, 5, 2, 67, 8, 4, 55, 8, 22, 3, 99, 567, 34, 567] # Example

def biggest_index(lst):
    biggest = lst[0]
    index = 0
    biggestIndex = 0
    for i in lst:
        if i > biggest:
            biggest = i
            biggestIndex = index
        index += 1
    return biggestIndex

def sortArr(arr):
    if len(arr) == 1:
        return arr.pop(biggest_index(arr))
    return str(arr.pop(biggest_index(arr))) + ', ' + str(sortArr(arr))

print(list(map(int, sortArr(arr).split(", "))))
