class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        key={0:[0,-1]}
        s=0
        for i in range(len(nums)):
            s+=nums[i]
            if k!=0:
                s%=k
            if s in key:
                if i-key[s][1]>1:
                    return True
            else:
                key[s]=[s,i]
        return False
    