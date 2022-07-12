class Solution:
    def makesquare(self, M: List[int]) -> bool:
        n, side = len(M), sum(M) / 4
        M.sort(reverse=True)
        if side != int(side) or M[0] > side:
            return False
        def btrack(i, space, done): 
            if done == 3:
                return True
            while i < n:
                num = M[i]
                if num > space:
                    i += 1
                    continue
                M[i] = side + 1
                if num == space:
                    res = btrack(1, side, done+1)
                else:
                    res = btrack(i+1, space-num, done)
                if res:
                    return True
                M[i] = num
                while i < n and M[i] == num:
                    i += 1
            return False
        return btrack(0, side, 0)