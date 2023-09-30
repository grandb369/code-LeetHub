class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack=[]
        mi=[]
        temp=nums[0]
        for i in nums:
            temp=min(i,temp)
            mi.append(temp)
        for i in range(len(nums)-1,-1,-1):
            if nums[i]>mi[i]:
                while stack and stack[-1]<=mi[i]:
                    stack.pop()
                if stack and nums[i]>stack[-1]:
                    return True
                stack.append(nums[i])
        return False