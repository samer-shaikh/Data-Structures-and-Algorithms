import ctypes

# ----------------------------------- List --------------------------------------
class Mylist:
    def __init__(self) -> None:
        self.size = 1
        self.n = 0

        self.A = self.__make_array(self.size)

    def __len__(self):
        return self.n
    
    def __str__(self) -> str:
        res = ''
        for i in range(self.n):
            res = res + str(self.A[i]) + ','
        return '[' + res[:-1] + ']'
    
    def __repr__(self) -> str:
        res = ''
        for i in range(self.n):
            res = res + str(self.A[i]) + ','
        return '[' + res[:-1] + ']'
    
    def __getitem__(self, key):
        if key > self.n:
            return "the index is out of range"
        elif key < 0:
            return self.A[self.n+key]
        else:
            return self.A[key]

    def __delitem__(self, key):
        
        if 0 < key < self.n:
            for i in range(key,self.n-1):
                self.A[i] = self.A[i+1]  
            self.n -= 1

    def __add__(self, other):
        for i in range(len(other)):
            self.append(other[i])
        
    
    def __make_array(self,capacity):
        return (capacity*ctypes.py_object)()
    
    def __reshape(self):
        new_size = self.size*2
        B = self.__make_array(new_size)
        self.size = new_size
        for i in range(len(self.A)):
            B[i] = self.A[i]
        self.A = B

    def append(self,item):
        if self.n == self.size:
            #reshape
            self.__reshape()      
        #append 
        self.A[self.n] = item
        self.n += 1

    def pop(self):
        if self.n == 0:
            return None
        pop_item = self.A[self.n-1]
        self.A[self.n-1] = None
        self.n -= 1
        return pop_item
    
    def clear(self):
        self.size = 1
        self.n = 0

    def find(self,item):
        for i in range(self.n):
            if self.A[i] == item:
                return i
            
        return 'value not found'
    
    def insert(self,val,index):
        if self.n == self.size:
            self.__reshape()
        
        for i in range(self.n,index-1,-1):
            self.A[i] = self.A[i-1]
        
        self.A[index] = val
        self.n += 1

    def remove(self,val):
        index = self.find(val)
        if type(index) == int:
            self.__delitem__(index)
        else:
            return index
        
    def min(self):
        min_val = self.A[0]
        for i in range(self.n):
            if self.A[i] < min_val:
                min_val = self.A[i]
        return min_val

    def max(self):
        max_val = 0
        for i in range(self.n):
            if self.A[i] > max_val:
                max_val = self.A[i]
        return max_val
    
    def sum(self):
        sum_val = 0
        for i in range(self.n):
            sum_val += self.A[i]
        return sum_val 
        

# ----------------------------------- Linked List --------------------------------------

class Node:

    def __init__(self,value):
        self.data = value
        self.next = None

class LinkedList:

    def __init__(self) -> None:
        
        #creating the empty list
        self.head = None

        # No of nodes in LinkedList
        self.n = 0

    def insert_head(self,value):
        
        # creat the new head
        new_head = Node(value)

        new_head.next = self.head

        self.head = new_head

        self.n += 1
    
    def len(self):
        return self.n

    def __str__(self) -> str:
        curr = self.head
        result = ''
 
        while curr != None:
            result = str(curr.data) + ' -> ' + result
            curr = curr.next
        
        return '[' + result[:-4] + ']'
    
    def __getitem__(self, key):
        
        curr = self.head
        pos = 0

        if key < 0:
            key = self.len() + key

        while curr != None:
            if pos == key:
                return curr.data
            curr = curr.next
            pos += 1
            
        raise IndexError('Index out of range') 
    
    def __delitem__(self, key):
        
        if self.n-1 < key:
            raise IndexError("Index out of range")
        if key < 0:
            key = self.n + key
        if key == 0:
            return self.remove_head()

        pos = 0
        curr = self.head
        while curr != None:
            if pos == key:
                self.remove(curr.data)
                return
            curr = curr.next
            pos += 1
          
    def add(self,value):

        new_node = Node(value)
        if self.head == None:
            self.head = new_node            
            self.n += 1
            return       
    
        curr = self.head
    
        while curr.next != None:
            curr = curr.next

        curr.next = new_node
        self.n += 1

    def insert(self,after,value):

        curr = self.head
        new_node = Node(value)

        while curr != None:
            if curr.data == after:
                break
            curr = curr.next
        
        if curr != None:
            new_node.next  = curr.next
            curr.next = new_node
            self.n += 1
        else:
            return 'Item not found'
    
    def clear(self):
        self.head = None
        self.n = 0

    def remove_head(self):
        if self.head == None:
            return "The Linkedlist is empty"
        self.head = self.head.next
        self.n -= 1

    def pop(self):

        if self.head == None:
            return 'the list is empty'

        curr = self.head

        if curr.next == None:
            self.remove_head()
            return

        while curr.next.next != None:
            curr = curr.next

        curr.next = None
        self.n -= 1

    def remove(self,value):

        if self.head.data == value:
            return self.remove_head()
        
        if self.head == None:
            return "The list is empty"

        curr = self.head

        while curr.next != None:
            
            if curr.next.data == value:
                curr.next = curr.next.next     
                curr = curr.next
                self.n -=1
                return 
            curr = curr.next

        return 'Item not found'
    
    def find(self, value):
        
        curr = self.head
        pos = 0
        while curr != None:
            if curr.data == value:
                return pos
            pos += 1
            curr = curr.next
        
        return "Item not found in Linked list."

    def replace(self,index,val):
        if self.n < index:
            raise IndexError("Index out of range.")
        if index < 0:
            index = self.n + index
        pos = 0
        curr = self.head
        while True:
            if pos == index:
                curr.data = val
                return
            curr = curr.next
            pos += 1
        
    def max(self):
        max_val = 0
        curr = self.head

        while curr != None:
            if curr.data > max_val:
                max_val = curr.data
            curr = curr.next
        return max_val
    
    def replace_max(self,val):
        max_val = self.max()
        max_index = self.find(max_val)
        self.replace(max_index,val)

# ----------------------------------- Stack --------------------------------------------

class Stack:

    def __init__(self) -> None:
        self.top = None
        self.n = 0

    def __repr__(self) -> str:

        if self.is_empty():
            return "Stack is empty"
        
        res = ""
        curr = self.top
        while curr != None:
            res = res + str(curr.data) + "->"
            curr = curr.next
        
        return res[:-2]
    
    def __str__(self) -> str:

        if self.is_empty():
            return "Stack is empty"
        res = ""
        curr = self.top
        while curr != None:
            res = res + str(curr.data) + "->"
            curr = curr.next
        
        return res[:-2]

    def is_empty(self) -> bool:
        return self.top == None
    
    def add(self,val):
        new_node = Node(val)
        new_node.next = self.top
        self.top = new_node

    def peek(self):

        if self.is_empty():
            return "Stack is empty"
        
        return self.top.data

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        pop_item = self.top.data
        self.top = self.top.next
        return pop_item
    
    def traverse(self):

        curr = self.top

        while curr != None:

            print(curr.data)
            curr = curr.next
    
# ----------------------------------- Queue -------------------------------------------

class Queue:

    def __init__(self) -> None:
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front == None
    
    def enqueue(self,val):

        new_node = Node(val)

        if self.is_empty():
            self.front = new_node

        self.rear.next = new_node
        self.rear = self.rear.next

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        data = self.front.data
        self.front = self.front.next
        return data
    
    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.front.data

    def traverse(self):

        if self.is_empty():
            return "Queue is empty"
        
        curr = self.front

        while curr != None:
            print(curr.data,end=' ')
            curr = curr.next

    def clear(self):
        self.front = None
        self.rear = None


