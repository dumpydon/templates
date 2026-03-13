class BIT:
    def __init__(self,arr):
        self.length=len(arr)+1
        self.stree = [0]*(len(arr)+1)
        
        for i, n in enumerate(arr):
            self.increase(i,n)

    def increase(self,i,x):
        while i<self.length:
            self.stree[i]+=x
            i |= (i+1)
    
    def total(self, i):
        s = 0

        while i>=0:
            s+=self.stree[i]
            i &= i+1
            i-=1
        return s
    
    def sum(self,a,b):
        return self.total(b) - self.total(a-1)

    def update(self,i,x):
        self.increase(i,x-self.sum(i,i))
 
