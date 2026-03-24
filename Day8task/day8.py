#intersection
arr1 = [1,2,3,4,5]
arr2 = [3,4,5,6,7]

a = set(arr1)
b = set(arr2)
c = a & b

print(list(c))

#selectionsort
def ss(arr):
    n = len(arr)
    for i in range(n):
        m = i
        for j in range(i + 1, n):
            if arr[j] < arr[m]:
                m = j
        arr[i], arr[m] = arr[m], arr[i]
    return arr

arr = [5, 2, 9, 1, 5, 6]
print(ss(arr))

#bubblesort
def bs(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j] 
    return arr

arr = [5, 2, 9, 1, 5, 6]
print(bs(arr))
