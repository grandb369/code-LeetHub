class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        p1=0
        n=len(nums)
        p2=len(nums)-1
        while p1<p2:
            while p1<p2 and nums[p1]%2==0:
                p1+=1
            while p1<p2 and nums[p2]%2==1:
                p2-=1
            if p1<p2 and nums[p1]%2 and nums[p2]%2==0:
                nums[p1],nums[p2]=nums[p2],nums[p1]
        return nums