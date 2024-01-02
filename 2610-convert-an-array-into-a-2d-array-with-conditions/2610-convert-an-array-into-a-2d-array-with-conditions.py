class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        k=collections.defaultdict(int)
        ma=0
        for i in nums:
            k[i]+=1
            ma=max(ma,k[i])
        out=[[] for i in range(ma)]
        for i in k:
            for j in range(k[i]):
                out[j].append(i)
        return out