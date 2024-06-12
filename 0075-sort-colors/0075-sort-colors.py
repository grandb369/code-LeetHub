class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        p1=0
        p2=n-1
        while p1<n and nums[p1]==0:
            p1+=1
        while p2>p1 and nums[p2]==2:
            p2-=1
        p=p1+1
        while p<p2:
            if nums[p]==0:
                nums[p1],nums[p]=nums[p],nums[p1]
                while p1<p2 and nums[p1]==0:
                    p1+=1
                p=max(p1+1,p)
            elif nums[p]==2:
                nums[p2],nums[p]=nums[p],nums[p2]
                while p1<p2 and nums[p2]==2:
                    p2-=1
            else:
                p+=1
        if p1<n and p2>=0 and (nums[p1]==2 or nums[p2]==0):
            nums[p1],nums[p2]=nums[p2],nums[p1]