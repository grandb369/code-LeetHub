class Solution:
    def mostPoints(self, nums: List[List[int]]) -> int:
        k=collections.deque([0 for i in range(10**5+2)])
        pre=0
        out=0
        for point,skip in nums:
            pre=max(pre,k.popleft())
            k.append(0)
            val=pre+point
            k[skip]=max(k[skip],val)
            out=max(out,val)
        return out