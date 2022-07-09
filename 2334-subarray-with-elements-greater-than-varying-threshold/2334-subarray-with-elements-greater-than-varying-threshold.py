class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        v=max(nums)
        if v>threshold:
            return 1
        if v*len(nums)<=threshold:
            return -1
        def check(nums,val):
            if len(nums)==1:
                return -1
            n=len(nums)
            v=val/n
            temp=[]
            nex=[]
            c=0
            while nums:
                cur=nums.pop()
                if cur<=v:
                    if temp:
                        nex.append(temp)
                        temp=[]
                    c+=1
                else:
                    temp.append(cur)
            if c==0:
                return n
            if temp:
                nex.append(temp)
            for i in nex:
                out=check(i,val)
                if out!=-1:
                    return out
            return -1
        return check(nums,threshold)
            