#Q. 1 Create a Stack with following operation

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class stack:
    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top is None

    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.isempty():
            print("Stack is empty")
        else:
            print("Popped element:", self.top.data)
            self.top = self.top.next

    def display(self):
        if self.isempty():
            print("Stack is empty")
        else:
            temp = self.top
            while temp:
                print(temp.data)
                temp = temp.next

    def reverse_string(self, s):
        temp = self.top
        rev = ""

        while temp:
            rev += temp.data
            temp = temp.next

        print("Reversed string:", rev)

    def reverse(self):
        temp = self.top

        while temp:
            st1.push(Node(temp.data))
            temp = temp.next

        print("Reversed stack:")
        st1.display()


st = stack()
st1 = stack()

st.push(Node(10))
st.push(Node(20))
st.push(Node(30))
st.push(Node(40))
st.push(Node(50))

print("Original stack:")
st.display()

st.reverse()
