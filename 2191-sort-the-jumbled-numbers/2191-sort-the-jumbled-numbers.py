class Solution:
    def sortJumbled(self, m: List[int], nums: List[int]) -> List[int]:
        temp={}
        for ind,i in enumerate(nums):
            val=''
            if i==0:
                val=str(m[i])
            while i>0:
                v=i%10
                val=str(m[v])+val
                i//=10
            temp[ind]=int(val)
        out=[]
        for i in sorted(temp.keys(),key=lambda x:temp[x]):
            out.append(nums[i])
        return out