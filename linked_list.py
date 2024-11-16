import numpy as np
import pandas as pd

# Linked List operations

# making of Node
class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

#Making of Linked List
class LinkedList:
    def __init__(self):
         self.head=None
         self.n=0

    #return size of the linked list
    def __len__(self):
        return self.n

    #to insert new value from head
    def insert_head(self,value):
        #new node
        new_node=Node(value)
        new_node.next=self.head
        self.head=new_node
        #whenever adding new node increment n
        self.n=self.n+1

    #to traverse a linked list
    def traverse(self):
        curr=self.head
        while curr!=None:
            print(curr.data)
            curr=curr.next

    #add element from the last
    def append(self,value):
        new_node=Node(value)
        if self.head==None:
            #empty
            self.head=new_node
            self.n=self.n+1
            return
        curr=self.head
        while curr.next!=None:
            curr=curr.next
        #you are at the last node
        curr.next=new_node
        self.n=self.n+1

    #insert a new element after a given value
    def insert_after(self,after,value):
        new_node=Node(value)
        curr=self.head
        while curr!=None:
            if curr.data==after:
                break
            curr=curr.next
            if curr!=None:
                new_node.next=curr.next
                curr.next=new_node
                self.n=self.n+1
            else:
                return 'Item not found'

    #delete a linked list
    def clear(self):
        self.head=None
        self.n=0

    #delete head of linked list
    def delete_head(self):

        if self.head==None:
            # empty list
            return 'Empty Linked List'
        self.head=self.head.next
        self.n=self.n-1

    #delete elements from the last
    def pop(self):
        if self.head==None:
            return 'empty linkedlist'
        curr=self.head
        if self.n==1:
            return self.delete_head()
        while curr.next.next!=None:
            curr=curr.next
        curr.next=None
        self.n=self.n-1

    #delete a specific value
    def remove(self,value):
        # when the linked list is empty
        if self.head==None:
            return 'Empty Linked List'

        # when we need to remove the first element in ll
        if self.head==value:
            return self.delete_head()

        # when we remove from the middle
        curr=self.head
        while curr.next!=None:
            if curr.next.data==value:
                break
            curr=curr.next
            #case 1 item found
            #case 2 item not found
            if curr.next==None:
                return 'Not Found'
            else:
                curr.next=curr.next.next
                self.n=self.n-1

    #search a specific item in linked list
    def search(self,item):
        curr=self.head
        pos=0
        while curr!=None:
            if curr.data==item:
                return pos
            curr=curr.next
            pos=pos+1

        return 'not found'

    #fetch value  from the given index
    def __getitem__(self,index):
        curr=self.head
        pos=0
        while curr!=None:
            if pos==index:
                return curr.data
            curr=curr.next
            pos=pos+1
        return 'Index Error'

# Making First Linked List Object
L=LinkedList()
a=Node(1)       #a is an object of class node we can access both attributes data and next
L.insert_head(1)
L.insert_head(2)
L.insert_head(3)
L.insert_head(4)
#print(len(L))
#L.traverse()
#L.append(5)
#L.insert_after(3,30)
L.traverse()
L.pop()
L.traverse()
