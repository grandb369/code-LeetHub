class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        val=0
        c=0
        n=len(nums)
        out=n+1
        temp=collections.deque()
        while nums:
            while nums and val<target:
                v=nums.pop()
                temp.append(v)
                val+=v
                c+=1
            while temp and val>=target:
                out=min(out,c)
                v=temp.popleft()
                val-=v
                c-=1
        return out if out!=n+1 else 0