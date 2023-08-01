class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.out=[]
        def back(l,r,temp,k):
            if k==0:
                self.out.append(temp)
            for i in range(l,r):
                back(i+1,r,temp+[i],k-1)
        for i in range(1,n+1):
            back(i+1,n+1,[i],k-1)
        return self.out