class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
        n1=collections.Counter(nums1)
        n2=collections.Counter(nums2)
        out=set(list((n1&n2).elements()))
        return list(out)