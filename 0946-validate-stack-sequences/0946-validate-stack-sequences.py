class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        popped.reverse()
        temp=[]
        for i in pushed:
            temp.append(i)
            while temp and temp[-1]==popped[-1]:
                temp.pop()
                popped.pop()
        return len(temp)==0