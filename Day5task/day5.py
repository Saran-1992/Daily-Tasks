#first repeating char
a = [1,2,3,4,2,5,3]

b = []

for c in a:
    if c in b:
        print(c)
        break
    else:
        b.append(c)

#binary search
nums = [1,2,3,4,5,6,7]
target = 5

left,right = 0, len(nums) -1

while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
        print(mid)
        break
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

#square root
target = 9

left,right = 1,target

while left <= right:
    mid = (left + right) // 2
    if mid*mid == target:
        print(mid)
        break
    elif mid*mid < target:
        left = mid + 1
    elif mid*mid > target:
        right = mid - 1
        
