#deleting a Node by value

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

def delete_by_value(head,target):

    if head.val == target:
        head.next.prev = None
        head = head.next
        return head
    curr = head

    while curr:
        if curr.next.val == target:
            n = curr.next.next
            curr.next =n
            if n:
                n.prev =curr
            return head
        
        curr = curr.next
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


traverse(delete_by_value(head,3))
