#designing a DLL

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

class MyDLL:
    def __init__(self):
        self.head = None
    
    def insert_at_head(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node   

    def insert_at_tail(self,val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:

            curr  = self.head
            while curr.next:
                curr = curr.next

            curr.next = new_node
            new_node.prev = curr

    def insert_at_index(self,index,val):
        new_node = Node(val)
        if index == 0:
            self.insert_at_head(val)
            return
        count = 0
        curr = self.head
        while curr:
            if count == index -1:
                new_node.next = curr.next
                new_node.prev = curr
                if curr.next:
                    curr.next.prev = new_node
                curr.next = new_node
                return
            count +=1
            curr = curr.next
        if not curr:
            print("index out to bounds")
            return
    def delete_at_index(self,index):
        if index == 0:
            self.head.next.prev = None
            self.head =self.head.next
        
        count = 0
        curr = self.head
        while curr.next:
            if count == index-1:
                a = curr.next.next
                curr.next = a
                if a:
                    a.prev = curr
                return
            count +=1
            curr = curr.next

    def delete_by_value(self,target):

        if self.head.val == target:
            self.head.next.prev = None
            self.head = self.head.next
            return 
        curr = self.head

        while curr:
            if curr.next.val == target:
                n = curr.next.next
                curr.next =n
                if n:
                    n.prev =curr
                return
            curr = curr.next
    


    def traverse(self):
        curr = self.head
        while curr:
            print(curr.val,end="-->")
            curr  = curr.next
        print(None)
        

a = MyDLL()
a.insert_at_head(1)
a.insert_at_tail(2)
a.insert_at_index(2,3)
a.traverse()
a.insert_at_index(4,4)
a.traverse()
a.delete_at_index(3)
a.traverse()

a.delete_by_value(3)
a.traverse()
