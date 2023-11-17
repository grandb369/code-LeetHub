class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums=collections.deque(sorted(nums))
        out=0
        while nums:
            v=nums.popleft()
            v+=nums.pop()
            out=max(out,v)
        return out