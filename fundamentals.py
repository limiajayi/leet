
def binarySearch(list, num):
    first = 0
    last = len(list)    
    mid = (first + last) // 2
    
    while first < last:
        if num == list[mid]:
            return mid
        elif num < list[mid]:
            last = mid - 1
            mid = (first + last) // 2
        elif num > list[mid]:
            first = mid + 1
            mid = (first + last) // 2
        else:
            mid = -1
            
    return mid


arr = [1, 2, 3, 4, 5, 6, 7]
print(binarySearch(arr, 7))