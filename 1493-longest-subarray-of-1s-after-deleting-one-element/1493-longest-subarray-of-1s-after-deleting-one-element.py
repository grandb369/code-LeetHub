class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        temp=[]
        pre=0
        while nums:
            val=nums.pop()
            if val==0:
                if pre!=0:
                    temp.append(pre)
                    pre=0
                temp.append(0)
            else:
                pre+=1
        if pre!=0:
            temp.append(pre)
        zero=0
        while temp and temp[0]==0:
            temp.pop(0)
            zero+=1
        while temp and temp[-1]==0:
            temp.pop()
            zero+=1
        if not temp:
            return 0
        out=float('-inf')
        for i in range(len(temp)):
            if temp[i]==0 and temp[i-1]!=0 and temp[i+1]!=0:
                zero+=1
                out=max(out,temp[i-1]+temp[i+1])
            else:
                out=max(out,temp[i])
        if not zero:
            return max(temp)-1
        return out if out!=float('-inf')else max(temp)