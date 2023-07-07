class Solution:
    def maxConsecutiveAnswers(self, nums: str, k: int) -> int:
        out=0
        n=len(nums)
        t=[]
        f=[]
        pre=0
        for i in range(n):
            if nums[i]=='T':
                pre+=1
            else:
                t.append(pre)
                pre=0
        if pre:
            t.append(pre)
        pre=0
        for i in range(n):
            if nums[i]=='F':
                pre+=1
            else:
                f.append(pre)
                pre=0
        f.append(pre)
        if len(t)<=k+1 or len(f)<=k+1:
            return n
        pre=0
        
        for i in range(k+1):
            pre+=t[i]
        out=max(out,pre+k)
        for i in range(k+1,len(t)):
            pre=pre+t[i]-t[i-k-1]
            out=max(out,pre+k)
        pre=0
        for i in range(k+1):
            pre+=f[i]
        out=max(out,pre+k)
        for i in range(k+1,len(f)):
            pre=pre+f[i]-f[i-k-1]
            out=max(out,pre+k)
        return out