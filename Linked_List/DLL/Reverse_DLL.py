#reverse a DLL

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

# BruteForce Solution (stack algorithm)
# T.c = O(n)
# S.c = O(n)
# links are not changed, changing Nodes values only
def reverse_DLL(head):
    lis = []
    curr =head
    while curr:
        lis.append(curr.val)
        curr = curr.next
    
    curr =head
    while curr:
        curr.val = lis.pop()
        curr = curr.next
    return head

# Optimal solution
# T.C = O(n)
# s.c = O(1)
def reverse_DLL1(head):
    if head == None or head.next == None:
        return head
    prev = None
    curr =head
    while curr:
        next_node = curr.next
        curr.next = prev
        curr.prev = next_node
        prev = curr
        curr = next_node
    
    return prev

def traverse(head):
    curr = head
    while curr:
        print(curr.val,end="-->")
        curr = curr.next
    print(None)
head =Node(1)
head.next  = Node(2)
head.next.prev = head
head.next.next = Node(3)
head.next.next.prev = head.next

traverse(head)
traverse(reverse_DLL(head))
traverse(reverse_DLL1(head))    
