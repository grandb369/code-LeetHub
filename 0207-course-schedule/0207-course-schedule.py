class Solution:
    def canFinish(self, n: int, p: List[List[int]]) -> bool:
        pren=[0 for i in range(n)]
        pre=collections.defaultdict(list)
        for i,j in p:
            pren[i]+=1
            pre[j].append(i)
        stack=[]
        for i in range(n):
            if pren[i]==0:
                stack.append(i)
        course=0

        while stack:
            val=stack.pop(0)
            for i in pre[val]:
                pren[i]-=1
                if pren[i]==0:
                    stack.append(i)
                course+=1
        return course==len(p)