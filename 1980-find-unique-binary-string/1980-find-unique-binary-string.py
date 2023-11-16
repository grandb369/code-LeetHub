class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        temp=set()
        for i in nums:
            temp.add(int(i,2))
        n=len(nums[0])
        v=2**(n)-1
        for i in range(17):
            if v not in temp:
                val= bin(v)[2:]
                val='0'*(n-len(val))+val
                return val
            if v-i not in temp:
                val= bin(v-i)[2:]
                val='0'*(n-len(val))+val
                return val