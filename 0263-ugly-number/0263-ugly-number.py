class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<0 or num==0:
            return False
        if num<=5:
            return True
        while num%2==0:
            num=num/2
            if num==1:
                return True
        while num%3==0:
            num=num/3
            if num==1:
                return True
        while num%5==0:
            num=num/5
            if num==1:
                return True
        return False