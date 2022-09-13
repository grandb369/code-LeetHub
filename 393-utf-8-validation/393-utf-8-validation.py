class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        nums=data[::-1]
        while nums:
            cur=bin(nums.pop())[2:]
            if cur[0]=='0'or len(cur)!=8:
                continue
            c=-1
            for i in range(min(4,len(cur))):
                if cur[i]=='1':
                    c+=1
                else:
                    break
            if len(cur)==8 and c==3 and cur[4]=='1':
                return False
            if c==0:
                return False
            if len(nums)<c:
                return False
            while c>0:
                val=bin(nums.pop())[2:]
                if val[:2]!='10' or len(val)!=8:
                    return False
                c-=1
        return True