class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        out=[]
        if not nums:
            return out
        elif not k:
            return nums
        temp=[nums[0]]
        for i in range(1,k):
            while len(temp):
                if nums[i]>temp[-1]:
                    temp.pop()
                else:
                    break
            temp.append(nums[i])
        for i in range(k,len(nums)):
            out.append(temp[0])
            if temp[0]==nums[i-k]:
                temp.pop(0)
            while len(temp):
                if nums[i]>temp[-1]:
                    temp.pop()
                else:
                    break
            temp.append(nums[i])
        out.append(temp[0])
        return out