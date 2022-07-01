class Solution:
    def maximumUnits(self, nums: List[List[int]], size: int) -> int:
        nums.sort(key=lambda x:x[1],reverse=True)
        out=0
        for i,j in nums:
            val=min(size,i)
            out+=val*j
            size-=val
            if size==0:
                break
        return out