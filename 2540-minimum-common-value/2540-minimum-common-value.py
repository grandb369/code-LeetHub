class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        out=set(nums1) & set(nums2)
        return min(out) if out else -1