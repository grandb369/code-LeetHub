class Solution:
    def findJudge(self, n: int, nums: List[List[int]]) -> int:
        temp1=[0 for i in range(n)]
        temp2=[0 for i in range(n)]
        for i,j in nums:
            temp1[i-1]+=1
            temp2[j-1]+=1
        for i in range(n):
            if temp2[i]==n-1 and temp1[i]==0:
                return i+1
        return -1