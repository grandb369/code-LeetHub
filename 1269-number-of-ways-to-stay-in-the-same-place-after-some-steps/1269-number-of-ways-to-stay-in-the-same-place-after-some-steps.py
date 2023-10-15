class Solution:
    def numWays(self, steps, arrLen):
        arrLen = min(arrLen, steps + 1) 
        f = [1]+[0]*(arrLen-1) # f[0] = 1

        for i in range(1, steps+1):
            old = 0 
            for j in range(arrLen):
                old_left = old
                old = f[j]
                if j > 0:
                    f[j] += old_left      
                if j < arrLen - 1:
                    f[j] += f[j+1]   
        return f[0] % (10 ** 9 + 7)