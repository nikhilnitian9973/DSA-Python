# Reverse a singly linked list

####   iterative solution

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None



def Reverse(head):
    curr = head
    prev = None
    while curr != None:
        next_Node = curr.next
        curr.next = prev
        prev = curr
        curr = next_Node
    head = prev
    return head

def traverse(head):
    curr = head

    while curr != None:
        print(curr.val,end="-->")
        curr = curr.next
    print(None)




# 1 --> 2 --> 3 --> 4 --> 5 --> 6 --> None

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)


traverse(Reverse(head))




### Recursive Solution

def reverse(head):
    
    
    def rev(curr= head,prev = None):
        if curr == None:
            return prev
        next_Node = curr.next
        curr.next = prev
        prev = curr
        curr = next_Node
        rev(curr,prev)
    return rev()
traverse(reverse(head))