#Duplicates in number
nums = [1,2,3,4,2,5,6,3]
seen = []
dup = []

for i in nums:
    if i in seen:
        dup.append(i)
    else:
        seen.append(i) 
        
print(dup)

#subarray length
str = "abcabcbb"
left = 0
m = 0
og = set()

for right in range(len(str)):
    while str[right] in og:
        og.remove(str[left])
        left += 1
    og.add(str[right])
    m = max(m , right - left + 1)
    
print(m)  

#unique char
str = "saranbabu"
count = {}

for i in str:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
        
for j in str:
    if count[j]  == 1:
        print(j)
