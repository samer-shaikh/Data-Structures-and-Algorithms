import ctypes

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
        

        
    