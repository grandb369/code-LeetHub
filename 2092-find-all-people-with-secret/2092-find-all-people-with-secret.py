class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        k=collections.defaultdict(set)
        for u,v,t in meetings:
            k[t].add((u,v))
        temp=set([0,firstPerson])
        for i in sorted(k.keys()):
            pre=1
            cur=set([])
            while pre!=0 and (cur or k[i]):
                pre=0
                if cur:
                    while cur:
                        u,v=cur.pop()
                        if u in temp or v in temp:
                            temp.add(u)
                            temp.add(v)
                            pre+=1
                        else:
                            k[i].add((u,v))
                else:
                    while k[i]:
                        u,v=k[i].pop()
                        if u in temp or v in temp:
                            temp.add(u)
                            temp.add(v)
                            pre+=1
                        else:
                            cur.add((u,v))
        return list(temp)