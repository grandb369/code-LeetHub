class Solution:
    def predictPartyVictory(self, nums: str) -> str:
        d=r=0
        for i in nums:
            if i=='R':
                r+=1
            else:
                d+=1
        nums=collections.deque(nums)
        db=rb=0
        while d and r:
            cur=nums.popleft()
            if cur=='D':
                if db:
                    db-=1
                    d-=1
                else:
                    rb+=1
                    nums.append(cur)
            else:
                if rb:
                    rb-=1
                    r-=1
                else:
                    db+=1
                    nums.append(cur)
        if r:
            return 'Radiant'
        return 'Dire'