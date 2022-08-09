class Solution:
    def countVowelPermutation(self, n: int) -> int:
        k={}
        mod=10**9+7
        for i in 'aeiou':
            k[i]=1
        for i in range(n-1):
            temp={}
            temp['e']=k['a']+k['i']
            temp['a']=k['e']+k['u']+k['i']
            temp['u']=k['o']+k['i']
            temp['i']=k['e']+k['o']
            temp['o']=k['i']
            k=temp
        return sum(k.values())%mod