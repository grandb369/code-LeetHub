class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if not amount:
            return 1
        dp=[0 for i in range(amount+1)]
        for i in coins:
            if i <=amount:
                dp[i]+=1
                for j in range(i+1,amount+1):
                    dp[j]+=dp[j-i]
        return dp[-1]