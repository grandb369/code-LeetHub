class Solution:
    def construct2DArray(self, nums: List[int], m: int, n: int) -> List[List[int]]:
        if len(nums)!=m*n:
            return []
        out=[]
        while nums:
            out.append(nums[:n])
            nums=nums[n:]
        return out