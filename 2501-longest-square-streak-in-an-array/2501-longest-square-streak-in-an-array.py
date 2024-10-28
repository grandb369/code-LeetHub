class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        k=collections.defaultdict(int)
        for i in nums:
            k[i**2]=max(k[i]+1,k[i**2])
        out=0
        for i in k:
            out=max(out,k[i])
        if out>1:
            return out
        return -1