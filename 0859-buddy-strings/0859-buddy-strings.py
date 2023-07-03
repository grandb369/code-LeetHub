class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        a=collections.Counter(A)
        b=collections.Counter(B)
        if a!=b:
            return False
        if A==B:
            for i in a.keys():
                if a[i]>1:
                    return True
            return False
        diff=0
        for i in range(len(A)):
            if A[i]!=B[i]:
                diff+=1
            if diff>2:
                return False
        return True