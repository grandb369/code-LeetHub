class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        lr=1
        h=q
        while h%p!=0:
            h+=q
            lr+=1
        if (h//p)%2==1:
            if lr%2:
                return 1
            return 2
        return 0