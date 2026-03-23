#array
a = [0,1,0,3,12]

left = 0

for right in range (len(a)):
    if a[right] != 0:
        a[left],a[right] = a[right],a[left]
        left += 1
        
print(a)    

#reverselist
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        
def reverselist (head):
    prev = None
    curr = head
    
    while curr!=None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        
    return prev
        
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

new_list = reverselist(node1)

temp = new_list
while temp != None:
    print(temp.val, end=" -> ")
    temp = temp.next
print("None")

#middle
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        
def middle (head):
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    return slow
        
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

middle_node = middle(node1)

if middle_node != None:
    print(middle_node.val)
