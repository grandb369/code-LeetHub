class Solution:
    def canCross(self, nums: List[int]) -> bool:
        k=collections.defaultdict(set)
        k[0]=set([0])
        target=nums[-1]
        for i in nums:
            if target in k:
                return True
            for j in k[i]:
                if i+j==target:
                    return True
                if j!=0:
                    k[i+j].add(j)
                if j-1>0:
                    k[i+j-1].add(j-1)
                k[i+j+1].add(j+1)
            del k[i]
        return False