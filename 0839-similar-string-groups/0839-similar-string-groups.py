class Solution:
    def numSimilarGroups(self, A: List[str]) -> int:
        m, n = len(A[0]), len(A)
        A = set(A)
        p, res = {s : s for s in A}, len(A) # p: parent
        def find(s):
            while s != p[s]: 
                p[s] = p[p[s]]
                s = p[s]
            return s
        def judge(a, b):
            cnt = 0
            for i, j in zip(a, b):
                if i != j:
                    if cnt < 2: cnt += 1
                    else: return False
            return cnt == 2
        if m > n:
            for a, b in itertools.combinations(A, 2): # O(m * n ^ 2)
                if judge(a, b):
                    ra, rb = find(a), find(b)
                    if ra != rb: res, p[ra] = res - 1, rb
        else: 
            for a in A: # O(n * m ^ 2)
                for i, j in itertools.combinations(range(m), 2):
                    b = a[:i] + a[j] + a[i + 1: j] + a[i] + a[j + 1:]
                    if b in A: 
                        ra, rb = find(a), find(b)
                        if ra != rb: res, p[ra] = res - 1, rb
        return res