class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        out=0
        for i in logs:
            v,_=i.split('/')
            if v=='.':
                continue
            if v=='..':
                if out>0:
                    out-=1
                continue
            out+=1
        return out