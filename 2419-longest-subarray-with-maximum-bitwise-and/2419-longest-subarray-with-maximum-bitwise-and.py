class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        pre=0
        c=0
        out=0
        v=0
        for i in nums:
            pre&=i
            c+=1
            if i>pre:
                pre=i
                c=1
            if pre>v:
                out=c
                v=pre
            elif pre==v:
                out=max(out,c)
        return out