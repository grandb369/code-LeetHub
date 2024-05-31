class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        temp=0
        for i in nums:
            temp^=i
        mask=1
        while mask&temp==0:
            mask=mask<<1
        n1=n2=0
        for i in nums:
            if i&mask==0:
                n1^=i
            else:
                n2^=i
        return [n1,n2]