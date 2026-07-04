#leetcode 707 problem
# designing a linked list
# traverse, insert, delete(by index and by value), add at head, add at tail, middle Node, reverse sll
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


    def traverse_sll(self):
        curr = self.head
        while curr != None:
            print(curr.val,end="-->")
            curr = curr.next
        print(None)

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
    

    # a prev variable can be use (initially prev = None)
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




        
    # a prev variable can be use (initially prev = None)
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
    
    # if value present in sll then delete 
    def delete_by_val(self,value):
        if self.head.val == value:
            self.head = self.head.next
        else:
            
            curr = self.head
            while curr.next != None:
                if curr.next.val == value:
                    curr.next = curr.next.next
                    return
                curr = curr.next
                
            
            print("value is not present in sll")




    # if there are two middle Node then return second middle Node
    def middle_Node(self):
        slow = self.head
        fast = self.head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        mid = slow
        return mid
    

    def reverse_sll(self):
        prev = None
        curr = self.head
        while curr != None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        self.head = prev
        

        


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

print(obj.get(0),obj.get(1),obj.get(2),obj.get(3),obj.get(4),obj.get(5),obj.get(6))

obj.traverse_sll()
obj.delete_by_val(2)
obj.traverse_sll()

obj.reverse_sll()
obj.traverse_sll()
print(obj.middle_Node().val)







