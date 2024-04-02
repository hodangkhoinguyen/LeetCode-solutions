# Union-find approach

class Union:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        parentX = self.find(x)
        parentY = self.find(y)
        if parentX != parentY:
            self.parent[parentY] = parentX

    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ans = n = len(isConnected)
        uf = Union(n)

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1 and not uf.connected(i, j):
                    ans -= 1
                    uf.union(i, j)
        return ans
