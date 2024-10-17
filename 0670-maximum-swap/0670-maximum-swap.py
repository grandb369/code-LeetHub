class Solution:
    def maximumSwap(self, num: int) -> int:
        num=list(str(num))
        num=list(map(int,num))
        n=len(num)
        temp=[0 for i in num]
        temp[-1]=num[-1]
        for i in range(n-2,-1,-1):
            temp[i]=max(num[i],temp[i+1])
        k={}
        for i in range(len(num)):
            k[num[i]]=i
        for i in range(n):
            if num[i]!=temp[i]:
                index=k[temp[i]]
                num[i],num[index]=num[index],num[i]
                break
        num=int(''.join(list(map(str,num))))
        return num