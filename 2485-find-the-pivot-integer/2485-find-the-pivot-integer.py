class Solution:
    def pivotInteger(self, n: int) -> int:
        left=[i+1 for i in range(n)]
        right=[i+1 for i in range(n)]
        for i in range(1,n):
            left[i]+=left[i-1]
            right[n-i-1]+=right[n-i]
        for i in range(n):
            if left[i]==right[i]:
                return i+1
        return -1