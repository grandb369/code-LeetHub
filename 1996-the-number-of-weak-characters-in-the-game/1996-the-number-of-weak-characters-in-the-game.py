class Solution:
    def numberOfWeakCharacters(self, nums: List[List[int]]) -> int:
        nums.sort(key=lambda x: (-x[0],x[1]))
        
        ans = 0
        cur = 0
        for _, d in nums:
            if d < cur:
                ans += 1
            else:
                cur = d
        return ans