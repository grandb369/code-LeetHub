class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        p1=p2=float('inf')
        for i in nums:
            if i<=p1:
                p1=i
            elif i<=p2:
                p2=i
            else:
                return True
        return False