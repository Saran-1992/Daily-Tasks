#intersection
arr1 = [1,2,3,4,5]
arr2 = [3,4,5,6,7]

a = set(arr1)
b = set(arr2)
c = a & b

print(list(c))

#selectionsort
arr = [5, 2, 9, 1, 5, 6]

for i in range(len(arr)):
    m = i
    for j in range(i+1,len(arr)):
        if arr[j] < arr[m]:
            m = j 
    arr[i],arr[m] = arr[m],arr[i]
    
print(arr)

#bubblesort
arr = [5, 2, 9, 1, 5, 6]

for i in range(len(arr)):
    for j in range(0,len(arr)-1-i):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
    
print(arr)
