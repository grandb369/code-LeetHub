class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        stack=[]
        for i in nums:
            temp=[]
            for cur in stack:
                temp.append(cur)
                j=len(cur)-1
                while j>=0 and i-cur[j]<k:
                    j-=1
                if j>=0 and i-cur[j]==k:
                    continue
                temp.append(cur+[i])
            temp.append([i])
            stack=temp
        return len(stack)