class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        elif len(nums)==2:
            if nums[0]!=nums[1]:
                return 2
            return 1
        temp=[]
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                temp.append(1)
            elif nums[i]<nums[i-1]:
                temp.append(0)
        if not temp:
            return 1
        pre=temp[0]
        c=1
        for i in range(1,len(temp)):
            if temp[i]!=pre:
                pre=temp[i]
                c+=1
        return c+1