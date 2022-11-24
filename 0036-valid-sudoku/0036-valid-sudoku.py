class Solution:
    def isValidSudoku(self, mat: List[List[str]]) -> bool:
        row=collections.defaultdict(set)
        col=collections.defaultdict(set)
        unit=collections.defaultdict(set)
        for r in range(9):
            for c in range(9):
                val=mat[r][c]
                if val=='.':
                    continue
                if val in row[r]:
                    return False
                if val in col[c]:
                    return False
                if val in unit[(r//3,c//3)]:
                    return False
                row[r].add(val)
                col[c].add(val)
                unit[(r//3,c//3)].add(val)
        return True