class Node:
        def __init__(self,value):
            self.data=value
            self.next=None

class stack:
    def __init__(self):
        self.top=None
    def isempty(self):
        return self.top is None
    def push(self,new_node):
         new_node.next=self.top
         self.top=new_node
    def pop(self):
        if self.isempty():
            print("stack is empty")
        else:
            temp=self.top
            print("poped element:",temp.data)
            self.top=self.top.next
            temp=None
    def print(self):
        if self.isempty():
         print("stack is empty")
        else:
            print("stack contains...")
            temp=self.top
            while temp:
                print(temp.data)
                temp=temp.next
    def  reverse(self):
            temp=self.top
            while temp:
                st1.push(Node(temp.data))
                temp=temp.next
        
                     

st=stack()
st1=stack()

st.push(Node(10))
st.push(Node(20))
st.push(Node(30))
st.push(Node(40))
st.push(Node(50))

st.reverse()

st1.print()
st.reverse_stack()
#st.pop()


def reverse_stack(s1):
    q1=queue()
    while not s1.isempty():
        q1.enqueue(s1.pop())
    q1.print()
    while not q1.isempty():
        s1.push(Node(q1.dequeue()))

    s1.print()    



