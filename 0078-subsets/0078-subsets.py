class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out=[]
        seen=[]
        def back(nums,temp,out):
            if nums not in seen:
                if sorted(temp) not in out:
                    out.append(sorted(temp))
                for i in range(len(nums)):
                    back(nums[:i]+nums[i+1:],temp+[nums[i]],out)
                seen.append(nums)
        back(nums,[],out)
        return list(out)