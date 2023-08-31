class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        temp=collections.defaultdict(int)
        for index,i in enumerate(ranges):
            if i !=0:
                left,right=index-i,index+i
                if left<0:
                    left=0
                if right>n:
                    right=n
                temp[left]=max(temp[left],right)
        if not temp:
            return -1
        out=index=cur=maxi=0
        while maxi<n:
            while index<=maxi:
                cur=max(cur,temp[index])
                index+=1
            if cur<=maxi:
                return -1
            out+=1
            maxi=cur
        return out