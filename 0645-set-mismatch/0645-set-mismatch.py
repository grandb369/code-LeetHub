class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        temp=set([])
        n=len(nums)
        su=(n*(n+1))//2
        out=-1
        for i in nums:
            if i in temp:
                out=i
            temp.add(i)
            su-=i
        return [out,out+su]