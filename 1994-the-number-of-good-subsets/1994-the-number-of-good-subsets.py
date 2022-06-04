class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        k=collections.defaultdict(int)
        one=0
        out=0
        mod=10**9+7
        #   2,3,5,7,11,13,17,19,23,29
        for i in nums:
            if i not in [1,4,8,9,12,16,18,20,24,25,27,28]:
                k[i]+=1
            if i==1:
                one+=1
        for i in k:
            out+=k[i]
            
        def back(num,c,pre):
            pre%=mod
            if c==0:
                return pre
            out=0
            for i in range(len(num)):
                out+=back(num[i+1:],c-1,pre*num[i])
            return out%mod
        nums=[]
        for i in [2,3,5,7,11,13,17,19,23,29]:
            if k[i]!=0:
                nums.append(k[i])
        m=len(nums)
        for i in range(2,m+1):
            for j in range(m+1-i):
                out+=back(nums[j+1:],i-1,nums[j])
                out%=mod
                
                
        def cal(val,num):
            nums=[]
            out=0
            for i in num:
                if k[i]!=0:
                    nums.append(k[i])
            m=len(nums)
            for i in range(1,m+1):
                pre=k[val]
                for j in range(m-i+1):
                    out+=back(nums[j+1:],i-1,nums[j]*pre)
                    out%=mod
            return out
        if k[6]:
            out+=cal(6,[5,7,11,13,17,19,23,29])
            out%=mod
        if k[10]:
            out+=cal(10,[3,7,11,13,17,19,23,29])
            out%=mod
        if k[14]:
            out+=cal(14,[3,5,11,13,17,19,23,29])
            out%=mod
        if k[15]:
            out+=cal(15,[2,7,11,13,17,19,23,29])
            out%=mod
        if k[21]:
            out+=cal(21,[2,5,11,13,17,19,23,29])
            out%=mod
        if k[22]:
            out+=cal(22,[3,5,7,13,17,19,23,29])
            out%=mod
        if k[26]:
            out+=cal(26,[3,5,7,11,17,19,23,29])
            out%=mod
        if k[30]:
            out+=cal(30,[7,11,13,17,19,23,29])
            out%=mod
            
            
            
        def cal2(v1,v2,num):
            out=0
            nums=[]
            for i in num:
                if k[i]!=0:
                    nums.append(k[i])
            m=len(nums)
            for i in range(1,m+1):
                pre=k[v1]*k[v2]
                for j in range(m-i+1):
                    out+=back(nums[j+1:],i-1,nums[j]*pre)
                    out%=mod
            out+=k[v1]*k[v2]
            out%=mod
            return out
        
        
        if k[10]and k[21]:
            out+=cal2(10,21,[11,13,17,19,23,29])
            out%=mod
        if k[14]and k[15]:
            out+=cal2(14,15,[11,13,17,19,23,29])
            out%=mod
        if k[15]and k[22]:
            out+=cal2(15,22,[7,13,17,19,23,29])
            out%=mod
        if k[15]and k[26]:
            out+=cal2(15,26,[7,11,17,19,23,29])
            out%=mod
        if k[21]and k[22]:
            out+=cal2(21,22,[5,13,17,19,23,29])
            out%=mod
        if k[21]and k[26]:
            out+=cal2(21,26,[5,11,17,19,23,29])
            out%=mod
            
        out*=2**(one)
        out%=mod
        return out