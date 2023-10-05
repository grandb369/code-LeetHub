class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        n1=n2=nums[0]
        c1=c2=0
        for i in nums:
            if i==n1:
                c1+=1
            elif i==n2:
                c2+=1
            else:
                if c1==0:
                    n1=i
                    c1=1
                elif c2==0:
                    n2=i
                    c2=1
                else:
                    c1-=1
                    c2-=1
        c1=c2=0
        for i in nums:
            if i==n1:
                c1+=1
            elif i==n2:
                c2+=1
        out=[]
        if c1>len(nums)//3:
            out.append(n1)
        if c2>len(nums)//3:
            out.append(n2)
        return out