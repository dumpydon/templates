class disjointset:
    def __init__(self, n):
        self.size = [1]*n
        self.parent = [i for i in range(n)]

    def find(self, x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv: return False #cycel / redundant edge found

        if self.size[pu] < self.size[pv]:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
        else:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
        return True    #union successful

    #______________________________________________________________________________
