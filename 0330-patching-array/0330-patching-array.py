class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        cur=0
        out=0
        nums.reverse()
        while nums and cur<n:
            while cur+1<nums[-1] and cur<n:
                cur=cur*2+1
                out+=1
            cur+=nums.pop()
        while cur<n:
            cur*=2
            cur+=1
            out+=1
        return out