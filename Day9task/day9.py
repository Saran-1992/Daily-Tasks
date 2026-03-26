#second laegest number
nums = [10, 5, 20, 8, 15]
s = sorted(nums)
print(s[-2])

#recursion
def f(n):
    if n<=1:return n
    
    return f(n-1) + f(n-2)
    
a = f(6)
print(a)
