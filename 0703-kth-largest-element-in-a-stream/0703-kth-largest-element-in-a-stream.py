from heapq import *
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.out = []
        self.cur = None
        self.k=k
        nums.sort(reverse=True)
        for i in range(min(len(nums),k-1)):
            heappush(self.out,nums[i])
        if k<=len(nums):
            self.cur = nums[k-1]
        
    def add(self, val: int) -> int:
        if self.cur!=None and val<self.cur:
            return self.cur
        if self.cur == val:
            return val
        heappush(self.out,val)
        if len(self.out)>=self.k:
            self.cur=heappop(self.out)
        return self.cur


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)