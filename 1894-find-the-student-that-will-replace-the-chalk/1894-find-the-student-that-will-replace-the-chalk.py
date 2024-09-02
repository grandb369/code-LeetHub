class Solution:
    def chalkReplacer(self, nums: List[int], k: int) -> int:
        su=sum(nums)
        k=k%su
        for i in range(len(nums)):
            if nums[i]>k:
                return i
            k-=nums[i]
        return 0