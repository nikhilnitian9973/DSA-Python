## find the length of cycle in a SLL


class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
# Brute Force solution

# T.C = O(n)
# S.C = O(n)

def length_cycle(head):
    my_dict = {}
    curr = head
    travel = 0
    while curr != None:
        if curr in my_dict:
            return travel - my_dict[curr] 
        my_dict[curr] = travel
        curr = curr.next
        travel +=1
    return 0
    

# optimal solution 

# T.C = O(n)
# s.c = O(1)

def length_cycle1(head):
    slow = head
    fast = head
    
    while fast != None and fast.next != None:
        slow =slow.next
        fast = fast.next.next
        
        if slow == fast:
            slow = slow.next
            count =1
            while slow != fast:
                count +=1
                slow = slow.next
            return count
    return 0

Node1 = Node(1)
Node2 = Node(2)
Node3 = Node(3)
Node4 = Node(4)

head = Node1
Node1.next = Node2
Node2.next = Node3
Node3.next = Node4
Node4.next = Node2


print(length_cycle(head))
print(length_cycle1(head))

