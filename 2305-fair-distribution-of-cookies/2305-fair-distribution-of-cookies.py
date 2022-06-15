class Solution:
    def distributeCookies(self, nums: List[int], k: int) -> int:
        def dfs(nums,temp):
            if not nums:
                return max(temp)
            out=float('inf')
            v=nums.pop()
            for j in range(k):
                if temp[j]+v>=out:
                    continue
                temp[j]+=v
                val=dfs(nums,temp)
                out=min(out,val)
                temp[j]-=v
            nums.append(v)
            return out
        temp=[0 for i in range(k)]
        return dfs(nums,temp)