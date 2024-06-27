class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        k=collections.defaultdict(int)
        n=len(edges)
        for i,j in edges:
            k[i]+=1
            k[j]+=1
            if k[i]==n:
                return i
            if k[j]==n:
                return j