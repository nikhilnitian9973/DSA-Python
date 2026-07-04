# return True if a sll have cycle otherwise return False


#### Brute Force solution
## T.C. -->> O(n) 
## S.C  -->> O(n)


class Node:
    def __init__(self,val):
        self.val  = val
        self.next = None
def hasCycle(head):
    my_set = set()
    curr = head
    while curr != None:
        if curr in my_set:
            return True
        my_set.add(curr)
        curr = curr.next
    return False

def hasCycle1(head):
    slow = head
    fast = head

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

Node1 = Node(1)
Node2 = Node(2)
Node3 = Node(3)
Node4 = Node(4)

head = Node1
Node1.next = Node2
Node2.next = Node3
Node3.next = Node4
Node4.next = Node2

print(hasCycle(head))
print(hasCycle1(head))

