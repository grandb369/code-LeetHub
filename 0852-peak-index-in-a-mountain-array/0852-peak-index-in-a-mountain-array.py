class Solution:
    def peakIndexInMountainArray(self, A: 'List[int]') -> 'int':
        
        p1=0
        p2=len(A)
        
        def BinarySearch(p1,p2,A):
            mid=(p1+p2)//2
            if mid==p1 or mid==p2:
                return p2
            if A[mid]>A[mid+1]:
                return BinarySearch(p1,mid,A)
            else:
                return BinarySearch(mid,p2,A)
            
        return BinarySearch(p1,p2,A)