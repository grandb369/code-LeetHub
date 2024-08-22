class Solution:
    def findComplement(self, num: int) -> int:
        base=1
        while base<=num:
            base*=2
        return (base-1)^num