#find middle Node of a singly linked list

## if there are two middle Node then return second middle Node


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class Solution:
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slow = head
        fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

a = Solution()
print(a.middleNode(head).val)

#other way for Nodes

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

head = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
print(a.middleNode(head).val)