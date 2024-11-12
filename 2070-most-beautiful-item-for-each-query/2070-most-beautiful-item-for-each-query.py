class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        k=collections.defaultdict(int)
        for i,j in items:
            k[i]=max(k[i],j)
        key=sorted(k.keys())
        for i in range(1,len(key)):
            k[key[i]]=max(k[key[i]],k[key[i-1]])
        out=[]
        for q in queries:
            l=0
            r=len(key)-1
            while l<r:
                mid=(l+r)//2
                if key[mid]==q:
                    l=mid
                    break
                elif key[mid]>q:
                    r=mid
                else:
                    l=mid+1
            if key[l]<=q:
                out.append(k[key[l]])
            else:
                if l==0:
                    out.append(0)
                else:
                    out.append(k[key[l-1]])
        return out