class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mask1=mask2=0
        for i in nums:
            mask1=~mask2&(mask1^i)
            mask2=~mask1&(mask2^i)
        return mask1