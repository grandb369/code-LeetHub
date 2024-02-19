class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return 2**32%n==0 if n>0 else False