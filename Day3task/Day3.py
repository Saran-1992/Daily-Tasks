#palindrome or not
a = 121
b = 0
c = a

while a > 0:
    r = a%10
    b = (b*10)+r
    a = a//10
    
if c==b:print("True")
else:print("False")

#space palindrome
a = "A man a plan a canal Panama"
b =  ""
for i in a.lower():
    if i != " ":
        b = i + b
        
if b ==b[::-1]:print("True")
else:print("False")

#reverse
a = "saran babu"
print(a[::-1])
