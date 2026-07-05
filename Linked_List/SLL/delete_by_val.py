#if value presents in sll then remove it
class Node():
    def __init__(self,val):
        self.val = val
        self.next =None
def delete_by_val(head,value):
    if head.val == value:
        head = head.next
        return head
    else:
        curr = head
        
        while curr.next != None:
            if curr.next.val == value:
                curr.next = curr.next.next
                return head
            curr = curr.next
        print("value does not present in sll")
        
def traverse_sll(head):
    curr = head
    while curr != None:
        print(curr.val,end="-->")
        curr = curr.next
    print(None)

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

head = delete_by_val(head,2)
traverse_sll(head)

