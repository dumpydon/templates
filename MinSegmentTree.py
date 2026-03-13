class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [inf] * (2 * self.n)

        for i in range(self.n):
            self.tree[self.n + i] = arr[i]

        for i in range(self.n - 1, 0, -1):
            self.tree[i] = min(self.tree[i << 1], self.tree[i << 1 | 1])

    def update(self, i, val):
        i += self.n
        self.tree[i] = val
        while i > 1:
            self.tree[i >> 1] = min(self.tree[i], self.tree[i ^ 1])
            i >>= 1

    def min(self, l, r):
        res = inf
        l += self.n
        r += self.n + 1
        while l < r:
            if l & 1:
                res = min(res, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                res = min(res, self.tree[r])
            l >>= 1
            r >>= 1
        return res

