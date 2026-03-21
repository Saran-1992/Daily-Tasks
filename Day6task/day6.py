#first non - repeating char
a = [4, 5, 1, 2, 0, 4, 1, 2]
counts = {}

for c in a:
    if c in counts:
        counts[c] += 1
    else:
        counts[c] = 1

for c in a:
    if counts[c] == 1:
        print(c)
        break
#two sum
nums = [2, 3, 4, 7, 11, 15]
target = 9

l = 0
r = len(nums) - 1

while l < r:
    cs = nums[l] + nums[r]
    
    if cs == target:
        print([l,r])
        break
    elif cs < target:
        l += 1
    else:
        r -= 1

#remove duplicates
nums = [1, 2, 2, 3, 4, 4, 4, 5]

u = []

for c in nums:
    if c not in u:
        u.append(c)

print(u)

a = set(nums)
print(a)
