
# arrange all even postion Node after all odd position Node without changing relative order inside odd and even postion Node.

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
## Brute Force Solution 1

# T.C. = O(n/2+n/2+n) = O(n)
# S.C = O(n)

def oddevenNode(head):

    lis = []
    odd = head
    while odd and odd.next:
        lis.append(odd.val)
        odd = odd.next.next
    if odd:
        lis.append(odd.val)
    even = head.next
    
    while even and even.next:
        lis.append(even.val)
        even = even.next.next
    
    curr = head
    count =0

    while count < len(lis):
        curr.val = lis[count]
        count +=1
        curr = curr.next
    return head


# Brute Force solution 2

# T.c = O(n/2+n/2+n)
#S.c = O(n)

def oddevenNode1(head):
    lis = []
    odd = head
    while odd and odd.next:
        lis.append(odd)
        odd = odd.next.next
    if odd:
        lis.append(odd)
    
    even = head.next

    while even and even.next:
        lis.append(even)
        even = even.next.next
    if even:
        lis.append(even)
    head = lis[0]
    curr =head
    
    for i in range(1, len(lis)):
        curr.next = lis[i]
        curr =curr.next
    curr.next = None

    return head


# Optimal solution

# T.C = O(n)
# S.C = O(1)

def oddevenNode2(head):
    if not head and not head.next:
        return head
    
    odd = head
    even = head.next
    even_head = head.next
    while even and even.next:
        odd.next = odd.next.next
        odd = odd.next
        
        even.next = even.next.next
        even = even.next
    odd.next = even_head
    return head

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

def traverse(head):
    curr = head
    while curr:
        print(curr.val,end="-->")
        curr =curr.next

print(traverse(oddevenNode(head)))
print(traverse(oddevenNode1(head)))
print(traverse(oddevenNode2(head)))