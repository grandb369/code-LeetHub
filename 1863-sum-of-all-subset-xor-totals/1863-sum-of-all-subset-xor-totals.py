class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans=0
        out = [[]]
        for num in nums:
            out += [i + [num] for i in out]
        for i in out:
            if i:
                v=0
                for j in i:
                    v^=j
                ans+=v
        return ans