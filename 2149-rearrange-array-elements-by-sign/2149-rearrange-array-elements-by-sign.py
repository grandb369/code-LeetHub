class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        po=[]
        ne=[]
        for i in nums:
            if i>=0:
                po.append(i)
            else:
                ne.append(i)
        out=[]
        for i in range(len(po)):
            out.append(po[i])
            out.append(ne[i])
        return out