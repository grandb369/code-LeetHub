class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(nums):
            if len(nums)<2:
                return nums
            n=len(nums)//2
            left=merge(nums[:n])
            right=merge(nums[n:])
            i=j=0
            out=[]
            while i<len(left) and j<len(right):
                if left[i]<=right[j]:
                    out.append(left[i])
                    i+=1
                else:
                    out.append(right[j])
                    j+=1
            while i<len(left):
                out.append(left[i])
                i+=1
            while j<len(right):
                out.append(right[j])
                j+=1
            return out
        return merge(nums)