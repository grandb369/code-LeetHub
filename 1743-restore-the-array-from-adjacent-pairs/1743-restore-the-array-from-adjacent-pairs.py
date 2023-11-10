class Solution:
    def restoreArray(self, a: List[List[int]]) -> List[int]:
        n=len(a)
        k=collections.defaultdict(set)
        seen=set([])
        for i,j in a:
            k[i].add(j)
            k[j].add(i)
            if i in seen:
                seen.remove(i)
            else:
                seen.add(i)
            if j in seen:
                seen.remove(j)
            else:
                seen.add(j)
        out=[seen.pop()]
        for i in range(n):
            cur=k[out[-1]].pop()
            k[cur].remove(out[-1])
            out.append(cur)
        return out