class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        one=s.count('1')
        n=len(s)
        z=n-one
        return '1'*(one-1)+'0'*z+'1'