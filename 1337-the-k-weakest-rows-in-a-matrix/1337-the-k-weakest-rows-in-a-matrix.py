class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        n=len(mat)
        m=len(mat[0])
        out=collections.defaultdict(int)
        for r in range(n):
            v=-1
            for c in range(m):
                if mat[r][c]==0:
                    break
                v=c
            out[r]=v+1
        return sorted(out,key=lambda x:out[x])[:k]