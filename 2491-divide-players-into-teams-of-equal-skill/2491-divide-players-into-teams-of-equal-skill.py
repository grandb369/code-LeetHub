class Solution:
    def dividePlayers(self, nums: List[int]) -> int:
        nums.sort()
        out=0
        nums=collections.deque(nums)
        pre=nums[0]+nums[-1]
        out+=nums[0]*nums[-1]
        nums.pop()
        nums.popleft()
        while nums:
            l=nums.popleft()
            r=nums.pop()
            if l+r!=pre:
                return -1
            out+=l*r
        return out