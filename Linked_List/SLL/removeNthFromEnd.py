#remove Nth Node from End 

class Node:
    def __init__(self,val):
        self.val =val
        self.next = None
# brute force solution

# T.C = O(n)
# S.C = O(1)

def removeNthFromEnd(head,n):
    len = 0
    curr =head
    while curr:
        len+=1
        curr = curr.next
    
    index = len-n
    if index ==0:
        return head.next
    
    count = 0
    curr = head
    while curr :
        if count == index -1:
            curr.next = curr.next.next
            return head
        curr = curr.next
        count +=1
    

# optimal solution

# T.C = O(n)
# T.c = O(1)

def removeNthFromEnd1(head,n):
    fast =head
    for i in range(n):
        fast = fast.next
    if fast == None:
        return head.next

    slow = head

    while fast.next:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next
    return head

def traverse(head):
    curr = head
    while curr:
        print(curr.val,end="-->")
        curr = curr.next

Node1 = Node(1)
Node2 = Node(2)
Node3 = Node(3)
Node4 = Node(4)
Node5 = Node(5)

head = Node1
Node1.next = Node2
Node2.next = Node3
Node3.next = Node4
Node4.next = Node5

print(traverse(removeNthFromEnd(head,2)))
print(traverse(removeNthFromEnd1(head,2)))
