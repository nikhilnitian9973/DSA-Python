#leetcode 707 problem
# designing a linked list

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        self.head = None

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if self.head is None:
            return  -1
        curr = self.head
        count = 0
        while curr != None:
            if count == index and curr != None:
                return curr.val
                
            count +=1
            curr = curr.next
        
        return -1


        

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node




        

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node = Node(val)
        if self.head is None:
            self.head =new_node
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = new_node
        

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        new_node = Node(val)
        
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            count = 0
            curr = self.head
            while curr is not None:
                if count == index -1:
                    new_node.next = curr.next
                    curr.next = new_node
                    return
                count +=1
                curr = curr.next




        

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        
        if index == 0:
            self.head = self.head.next
        else:
            
            count = 0
            curr = self.head
            while curr.next is not None:
                if count == index-1:
                    curr.next = curr.next.next
                    return
                count +=1
                curr = curr.next


        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

obj = MyLinkedList()
e1 = obj.addAtHead(1)
e2 = obj.addAtHead(2)
e3 = obj.addAtTail(4)
e4 = obj.addAtTail(3)
e5 = obj.addAtIndex(1,10)
dele = obj.deleteAtIndex(3)
print(obj.get(0))
print(obj.get(1))
print(obj.get(2))
print(obj.get(3))
print(obj.get(4))
print(obj.get(5))

