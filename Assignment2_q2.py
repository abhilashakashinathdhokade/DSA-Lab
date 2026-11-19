#Q. 2 Write a program to perform the following operations on a Linear Queue

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isempty(self):
        return self.front is None

    # 1. Enqueue
    def enqueue(self, value):
        new_node = Node(value)

        if self.isempty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    # 2. Dequeue
    def dequeue(self):
        if self.isempty():
            print("Queue is empty")
        else:
            print("Deleted element:", self.front.data)
            self.front = self.front.next

            if self.front is None:
                self.rear = None

    # 3. Display
    def display(self):
        if self.isempty():
            print("Queue is empty")
        else:
            temp = self.front

            while temp:
                print(temp.data)
                temp = temp.next

    # 4. Reverse using Stack
    def reverse(self):
        temp = self.front
        st = []

        while temp:
            st.append(temp.data)
            temp = temp.next

        self.front = self.rear = None

        while len(st) > 0:
            self.enqueue(st.pop())

    # 5. Merge two queues
    def merge(self, q2):
        temp = q2.front

        while temp:
            self.enqueue(temp.data)
            temp = temp.next

    # 6. Check identical queues
    def identical(self, q2):
        t1 = self.front
        t2 = q2.front

        while t1 and t2:
            if t1.data != t2.data:
                print("Queues are not identical")
                return

            t1 = t1.next
            t2 = t2.next

        if t1 is None and t2 is None:
            print("Queues are identical")
        else:
            print("Queues are not identical")

q1 = Queue()
q2 = Queue()

# Enqueue
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)

print("First Queue:")
q1.display()

# Dequeue
q1.dequeue()

print("After Dequeue:")
q1.display()

# Reverse
q1.reverse()

print("After Reverse:")
q1.display()

# Second Queue
q2.enqueue(30)
q2.enqueue(20)

# Identical
q1.identical(q2)

# Merge
q1.merge(q2)

print("After Merging:")
q1.display()
