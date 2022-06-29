class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        out=[[]for i in range(len(people))]
        pos=[i for i in range(len(people))]
        k=collections.defaultdict(list)
        for i,j in people:
            k[i].append(j)
        for i in sorted(k.keys()):
            val=sorted(k[i])
            while val:
                ind=val.pop()
                out[pos.pop(ind)]=[i,ind]
        return out