class Solution:
    def isNStraightHand(self, nums: List[int], m: int) -> bool:
        n=len(nums)
        if n%m:
            return False
        k=collections.defaultdict(int)
        for i in nums:
            k[i]+=1
        
        nums.sort(reverse=True)
        while nums:
            cur=nums.pop()
            while k[cur]==0 and nums:
                cur=nums.pop()
            if k[cur]==0:
                break
            k[cur]-=1
            n-=1
            for i in range(m-1):
                cur+=1
                if k[cur]==0:
                    return False
                k[cur]-=1
                n-=1
            
        return n==0