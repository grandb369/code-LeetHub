class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        temp=collections.defaultdict(int)
        for i in s:
            temp[i]+=1
        for i in t:
            if i not in temp:
                return i
            temp[i]-=1
            if temp[i]==0:
                del temp[i]