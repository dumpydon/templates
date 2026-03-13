class SortedPrefixSumList:
    def __init__(self,k):
        self.k = k
        self.sl = SortedList()
        self.S = 0
    
    def add(self,x):
        if len(self.sl)<self.k:
            self.S+=x
        elif x < self.sl[self.k-1]:
            self.S+=x-self.sl[self.k-1]
        self.sl.add(x)
    
    def remove(self,x):
        if self.sl.index(x) < self.k:
            self.S-=x
            self.sl.remove(x)
            self.S+=self.sl[self.k-1]
        else:
            self.sl.remove(x)
    
    def query(self):
        return self.S
