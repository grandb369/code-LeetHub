class Solution:
    def commonChars(self, nums: List[str]) -> List[str]:
        pre=[]
        n=len(nums)
        for i in range(n):
            cur=[0 for i in range(26)]
            for j in nums[i]:
                v=ord(j)-97
                cur[v]+=1
                if pre:
                    cur[v]=min(cur[v],pre[v])
            pre=cur
        out=[]
        for i in range(26):
            if pre[i]:
                out+=[chr(97+i)]*pre[i]
        return out