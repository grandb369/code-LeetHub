class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        k=collections.defaultdict(list)
        for i,j in enumerate(nums):
            k[j].append(i)
        nums.sort()
        su=0
        n=len(nums)
        m=n-1
        out=[0 for i in range(n)]
        su=sum(nums)
        pre=0
        for i in range(n):
            val=su-nums[i]*(n-i)+nums[i]*i-pre
            out[k[nums[i]].pop()]=val
            pre+=nums[i]
            su-=nums[i]
        return out