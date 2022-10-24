class Solution:
    def maxLength(self, arr: List[str]) -> int:
        nums=[]
        for i in arr:
            temp=['0'for j in range(26)]
            valid=True
            for j in i:
                val=ord(j)-ord('a')
                if temp[val]=='0':
                    temp[val]='1'
                else:
                    valid=False
            if valid:
                nums.append(''.join(temp))
        self.out=0
        n=len(nums)
        def back(pre,l):
            for i in range(l,n):
                v2=int(nums[i],2)
                if pre&v2==0:
                    v=pre|v2
                    self.out=max(self.out,bin(v).count('1'))
                    back(v,i+1)
        back(0,0)
        return self.out
                    