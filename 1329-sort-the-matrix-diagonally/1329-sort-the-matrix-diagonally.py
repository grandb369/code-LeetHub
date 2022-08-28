class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        k=collections.defaultdict(list)
        n=len(mat)
        m=len(mat[0])
        for r in range(n):
            for c in range(m):
                k[r-c].append(mat[r][c])
        for i in k:
            k[i].sort(reverse=True)
        for r in range(n):
            for c in range(m):
                mat[r][c]=k[r-c].pop()
        return mat