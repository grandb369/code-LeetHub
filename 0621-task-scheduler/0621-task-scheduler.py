class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        k=collections.Counter(tasks)
        if n==0:
            return len(tasks)
        key=sorted(k.keys(),key=lambda x:k[x],reverse=True)
        out=[''for i in range((n+1)*len(tasks))]
        pre=0
        while key:
            for i in range(min(len(key),n+1)):
                out[pre+i]=key[i]
                k[key[i]]-=1
                if k[key[i]]==0:
                    del k[key[i]]
            key=sorted(k.keys(),key=lambda x:k[x],reverse=True)
            pre+=n+1
        while out[-1]=='':
            out.pop()
        return len(out)