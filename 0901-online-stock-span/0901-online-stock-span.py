class StockSpanner:

    def __init__(self):
        self.out=[]
        self.data=[]

    def next(self, price: int) -> int:
        i=len(self.data)-1
        if self.data and self.data[-1]<=price:
            while i>=0 and self.data[i]<=price:
                i-=self.out[i]
            self.out.append(len(self.out)-i)
        else:
            self.out.append(1)
        self.data.append(price)
        return self.out[-1]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)