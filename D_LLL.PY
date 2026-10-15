
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None

class Doubly_LLL:
    def __init__(self):
     self.head=None

    def append(self,newnode):
        temp=self.head
        if temp:
            while temp.next:
                temp=temp.next
            temp.next=newnode
            newnode.prev=temp 
        else: #first node
            self.head=newnode
    def insert(self, new_node, pos):
            temp=self.head
            if pos==1:
                new_node.next=self.head
                if self.head:
                 self.head=new_node
            else:
                p=1
                while(p!=pos-1):
                    temp=temp.next
                    p+=1
                new_node.next=temp.next
                if temp.next: #Last Position
                 temp.next.prev=new_node
                temp.next=new_node
                new_node.prev=temp

    def print(self):
            temp=self.head
            print("List elements:", end=" ")
            while temp:
                print(temp.data, end=" ")
                temp=temp.next
            print()


list1=Doubly_LLL()
list1.append(Node(12))
list1.append(Node(52))
list1.append(Node(102))
list1.append(Node(56))
list1.append(Node(78))
list1.print()

list1.insert(Node(5),1)
list1.insert(Node(25),3)
list1.print()




    


















