class Graph:
    def __init__(self, n: int):
        self.n = n
        self.parent = [i for i in range(n)]
        self.compSize = [1 for i in range(n)]
    
    def getParent(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        self.parent[x] = self.getParent(self.parent[x])
        return self.parent[x]
    
    def unionSet(self, x: int, y: int):
        parx, pary = self.getParent(x), self.getParent(y)
        if parx != pary:
            if self.compSize[parx] < self.compSize[pary]:
                parx, pary = pary, parx
            self.parent[pary] = parx
            self.compSize[parx] += self.compSize[pary]
    
    def addEdge(self, x: int, y: int):
        self.unionSet(x, y)
    
    def isConnected(self) -> bool:
        return self.compSize[self.getParent(0)] == self.n


class Solution:
    def getPrimeFactors(self, x: int) -> int:
        for i in range(2, int(sqrt(x)) + 1):
            if x % i == 0:
                while x % i == 0:
                    x //= i
                yield i
        if x != 1:
            yield x
    
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        g = Graph(n)
        seen = {}
        for i in range(n):
            if nums[i] == 1:
                return False
            for prime in self.getPrimeFactors(nums[i]):
                if prime in seen:
                    g.addEdge(i, seen[prime])
                else:
                    seen[prime] = i
        return g.isConnected()