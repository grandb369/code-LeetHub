from heapq import *
class SeatManager:

    def __init__(self, n: int):
        self.data=[]
        for i in range(1,n+1):
            heappush(self.data,i)
        self.temp=set([])

    def reserve(self) -> int:
        val=heappop(self.data)
        self.temp.add(val)
        return val

    def unreserve(self, n: int) -> None:
        if n in self.temp:
            self.temp.remove(n)
            heappush(self.data,n)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)