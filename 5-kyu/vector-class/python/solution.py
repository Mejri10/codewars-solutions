class Vector:
    def __init__(self,arr):
        self.arr = arr
    
    def add(self,other):
        if len(self.arr) != len(other.arr):
            raise Exception
        return Vector([i+j for (i,j) in zip(self.arr,other.arr)])
        
    def subtract(self,other):
        if len(self.arr) != len(other.arr):
            raise Exception
        return Vector([i-j for (i,j) in zip(self.arr,other.arr)])
        
    def dot(self,other):
        if len(self.arr) != len(other.arr):
            raise Exception
        return sum([i*j for (i,j) in zip(self.arr,other.arr)])
        
    def norm(self):
        return sum([i**2 for i in self.arr])**0.5
        
    def __str__(self):
        return "(%s)" % ",".join([str(i) for i in self.arr])       
    
    def equals(self,other):
        if False in [i==j for (i,j) in zip(self.arr,other.arr)]:
            return False
        else:   
            return True