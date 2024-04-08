class Solution:
    def countStudents(self, students: List[int], s: List[int]) -> int:
        k=collections.defaultdict(int)
        n=len(s)
        m=len(students)
        for i in students:
            k[i]+=1
        s=s[::-1]
        while s:
            val=s[-1]
            if k[val]>0:
                k[val]-=1
                s.pop()
            else:
                break
        val=n-len(s)
        return m-val