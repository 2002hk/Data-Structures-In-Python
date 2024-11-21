class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
class queue:
    def __init__(self):
        self.front=None
        self.rear=None

    #insertion of element from the rear side
    def enqueue(self,value):
        new_node=Node(value)
        if self.front==None:
            self.front=new_node
            self.rear=new_node
        else:
            self.rear.next=new_node
            self.rear=new_node

    #deletion of element from the front side
    def dequeue(self):
        if self.front==None:
            return 'Empty'
        else:
            self.front=self.front.next

    #to check if the queue is empty
    def is_empty(self):
        return self.front==None

    #to see the front item in an queue
    def front_item(self):
        if(not self.is_empty()):
            return self.front.data
        else:
            return'Empty'

    #to see the rear item in the queue
    def rear_item(self):
        if(not self.is_empty()):
            return self.rear.data
        else:
            return 'Empty'

    #to traverse the queue
    def traverse(self):
        temp=self.front
        while temp!=None:
            print(temp.data,end=' ')
            temp=temp.next

    #to find the size of the queue
    def size(self):
        temp=self.front
        counter=0
        while temp!=None:
            counter=counter+1
            temp=temp.next
        return counter

q=queue()
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.traverse()