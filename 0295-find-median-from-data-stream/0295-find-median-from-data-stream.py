from sortedcontainers import SortedList
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data=SortedList([])
        self.n=0
        

    def addNum(self, num: int) -> None:
        self.data.add(num)
        self.n+=1

    def findMedian(self) -> float:
        n=self.n
        if self.n%2:
            return self.data[n//2]
        return (self.data[n//2-1]+self.data[n//2])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()