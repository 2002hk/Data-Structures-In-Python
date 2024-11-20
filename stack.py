class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class stack:
    def __init__(self):
        self.top=None

    #Empty stack or not
    def is_empty(self):
        return self.top==None

    #push value in stack
    def push(self,value):
        new_node=Node(value)
        new_node.next=self.top
        self.top=new_node

    #pop value from the top of the stack
    def pop(self):
        if self.top is None:
            return 'Stack Empty'
        else:
            data=self.top.data
            self.top=self.top.next
            return data

    #see the current top value in stack
    def peek(self):
        if self.top is None:
            return 'Empty Stack'
        else:
            return self.top.data

    #traverse a stack
    def traverse(self):
        temp=self.top
        while temp is not None:
            print(temp.data,end='')
            temp= temp.next

    #to return the current size of the stack
    def size(self):
        temp=self.top
        counter=0
        while temp is not None:
            temp=temp.next
            counter+=1
        return counter


#return reverse of the string
def reverse_string(string):
    s=stack()
    for i in string:
        s.push(i)
    res=''
    while (not s.is_empty()):
        res=res+s.pop()
    print(res)

#doing undo and redo operations
def text_editor(text,pattern):
    u=stack()
    r=stack()
    for i in text:
        u.push(i)
    for i in pattern:
        if i=='u':
            data=u.pop()
            r.push(data)
        else:
            data=r.pop()
            u.push(data)
        res=''
        while (not u.is_empty()):
            res=u.pop()+res
        print(res)
