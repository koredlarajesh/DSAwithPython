class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class single_ll:
    def __init__(self):
        self.head=None
    def insert_at_start(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head=new_node
    def verify_node(self,search):
        if self.head is None:
            return "no elments in the linked list"
        else:
            curr=self.head
            count=0
            while curr!=None:
                if curr.data==search:
                    return count+1
                count = count + 1
                curr=curr.next
            return -1
    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            curr=self.head
            while curr.next!=None:
                curr=curr.next
            curr.next=new_node

    def length_linked_list(self):
        if self.head==None:
            return 0
        else:
            count=0
            curr=self.head
            while curr!=None:
                count=count+1
                curr=curr.next
            return count
    def insert_at_pos(self,pos,data):
        new_node=Node(data)
        curr=self.head
        prev=None
        a=self.length_linked_list()
        count=0
        if pos==1:
            if self.head is None:
                self.head=new_node
            else:
                new_node.next=self.head
                self.head=new_node
        if pos==a:
            self.insert_at_end(data)
        else:
            while count<pos-1:
                prev=curr
                curr=curr.next
                count=count+1
            prev.next = new_node
            new_node.next=curr


    def display(self):
        if self.head is None:
            return "No elements in the linked list"
        else:
            curr=self.head
            while curr!=None:
                print(curr.data,end = " ",)
                curr=curr.next
sll = single_ll()
sll.insert_at_start(40)
sll.insert_at_start(30)
sll.insert_at_start(20)
sll.insert_at_start(10)
sll.insert_at_start(5)
sll.insert_at_end(2)
sll.insert_at_pos(3,21)
print(f'no of elements in the linked list {sll.length_linked_list()}')
print(f"\nverifying the element {sll.verify_node(30)}")
print(f"verifying the element {sll.verify_node(2)}")
print(f"verifying the element {sll.verify_node(5)}")
sll.display()


