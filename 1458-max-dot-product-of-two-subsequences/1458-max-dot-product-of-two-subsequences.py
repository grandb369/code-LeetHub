class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        dp=[[0 for i in range(len(nums2))]for i in range(len(nums1))]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                dp[i][j]=nums1[i]*nums2[j]
        for r in range(len(nums1)-2,-1,-1):
            dp[r][len(nums2)-1]=max(dp[r][len(nums2)-1],dp[r+1][len(nums2)-1])
        for c in range(len(nums2)-2,-1,-1):
            dp[len(nums1)-1][c]=max(dp[len(nums1)-1][c],dp[len(nums1)-1][c+1])
        for r in range(len(nums1)-2,-1,-1):
            for c in range(len(nums2)-2,-1,-1):
                dp[r][c]=max(dp[r][c],dp[r][c]+dp[r+1][c+1],dp[r+1][c],dp[r][c+1])
        return dp[0][0]