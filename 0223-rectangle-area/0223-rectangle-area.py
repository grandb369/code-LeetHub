class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int: 
        out=(D-B)*(C-A)+(H-F)*(G-E)
        additional=max((min(H,D)-max(B,F)),0)*max(0,(min(G,C)-max(A,E)))
        return out-additional
        