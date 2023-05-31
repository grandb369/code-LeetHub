class UndergroundSystem(object):

    def __init__(self):
        self.time=collections.defaultdict(list)
        self.cus={}

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.cus[id]=[stationName,t]

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        pre,pret=self.cus[id]
        del self.cus[id]
        name=pre+'-'+stationName
        time=t-pret
        self.time[name].append(time)

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        name=startStation+'-'+endStation
        su=sum(self.time[name])
        ans=operator.truediv(su,len(self.time[name]))
        return ans


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)