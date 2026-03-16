
#missing number
a = [1,2,3,4,6,7,8]
b = sum(a)
c = len(a)+1
d = c*(c+1)/2
print(d-b)

#two sum
nums = [2,7,11,15]
target = 9

right = nums[1]
left = nums[0]

for i in nums:
    if right+left==target:
        print(nums.index(left),nums.index(right))
        break
    else:
        right+=1
        left+=1

#maximum element in a array
nums = [2,7,11,150,100]
stack = []
for i in nums:
    if stack != []:
        if stack[-1]<i:
            stack.pop()
            stack.append(i)
    else:
        stack.append(i)
            
print(stack)        
