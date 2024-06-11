class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr=set(arr2)
        left=collections.defaultdict(int)
        right=[]
        for i in arr1:
            if i in arr:
                left[i]+=1
            else:
                right.append(i)
        out=[]
        for i in arr2:
            out+=[i]*left[i]
        return out+sorted(right)