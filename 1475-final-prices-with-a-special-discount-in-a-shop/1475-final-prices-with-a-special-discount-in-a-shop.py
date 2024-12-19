class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        out=[i for i in prices]
        stack=[]
        for i in range(len(prices)-1,-1,-1):
            while stack and stack[-1]>prices[i]:
                stack.pop()
            val=0
            if stack:
                val=stack[-1]
            out[i]-=val
            stack.append(prices[i])
        return out