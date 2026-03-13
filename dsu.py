class DSU:

    def __init__(self, N):
        self.parent=list(range(N))
    
    def find(self, x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        self.parent[self.find(x)]=self.find(y)
    
    def components(self):
        return len(set(self.find(i) for i in range(len(self.parent))))