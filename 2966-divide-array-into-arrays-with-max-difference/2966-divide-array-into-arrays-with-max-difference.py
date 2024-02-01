class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n=len(nums)
        if n%3!=0:
            return []
        nums.sort()
        out=[]
        while nums:
            v1=nums.pop()
            v2=nums.pop()
            v3=nums.pop()
            if v1-v3>k:
                return []
            out.append([v1,v2,v3])
        return out