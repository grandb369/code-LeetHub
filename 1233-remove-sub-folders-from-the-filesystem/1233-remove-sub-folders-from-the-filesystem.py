class Solution:
    def removeSubfolders(self, nums: List[str]) -> List[str]:
        tree={}
        for s in nums:
            s=s.split('/')[1:]
            t=tree
            for cur in s:
                if cur not in t:
                    t[cur]={'leaf':False}
                t=t[cur]
            t['leaf']=True
        out=[]
        def check(s,t):
            s.pop()
            for cur in s:
                t=t[cur]
                if t['leaf']:
                    return False
            return True
        for i in nums:
            s=i.split('/')[1:]
            if check(s,tree):
                out.append(i)
        return out