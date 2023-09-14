class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        k=collections.defaultdict(list)
        for i,j in sorted(tickets)[::-1]:
            k[i].append(j)
        stack=['JFK']
        out=[]
        while stack:
            while k[stack[-1]]:
                stack.append(k[stack[-1]].pop())
            out.append(stack.pop())
        return out[::-1]