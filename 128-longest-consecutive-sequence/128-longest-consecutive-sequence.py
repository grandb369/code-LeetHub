class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        out=0
        nums=set(nums)
        for i in nums:
            if i-1 not in nums:
                j=i+1
                while j in nums:
                    j+=1
                out=max(out,j-i)
        return out