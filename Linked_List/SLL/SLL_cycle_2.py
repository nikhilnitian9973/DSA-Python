## find the starting Node in cycle present in SLL

class Node:
    def __init__(self,val):
        self.val = val 
        self.next = None

## Brute Force solution

# T.C. -->> O(n)
# S.C. -->> O(n)

def find_starting_Node(head):
    my_set = set()
    curr = head

    while curr != None:
        if curr in my_set:
            return curr
        my_set.add(curr)
        curr = curr.next
    return None


## Optimal Solution

# T.C. -->> O(n)
# S.C. -->> O(1)

def find_starting_Node1(head):
    slow = head
    fast = head

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            slow = head

            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None

Node1 = Node(1)
Node2 = Node(2)
Node3 = Node(3)
Node4 = Node(4)

head = Node1
Node1.next = Node2
Node2.next = Node3
Node3.next = Node4
Node4.next = Node2

print(find_starting_Node(head).val)
print(find_starting_Node1(head).val)