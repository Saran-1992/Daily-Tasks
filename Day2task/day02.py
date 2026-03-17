#reverse number
nums = 1234
rn=0
while nums >0:
    r=nums%10
    rn=(rn*10)+r
    nums=nums//10
print(rn)

#Kadane's Algorithm
nums = [-2,1,-3,4,-1,2,1,-5,4]
cs = 0
m = nums[0]
    
for num in nums:
    cs += num
    m = max(m, cs)
        
    if cs < 0:
        cs = 0
            
print(m)

#second maximum
a = [5,8,2,10,7]
a.sort()
print(a[-2])
