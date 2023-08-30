class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        out=0
        pre=0
        while nums:
            cur=nums.pop()
            if pre==0 or cur<=pre:
                pre=cur
            else:
                v=cur//pre
                if cur%pre:
                    val=cur%pre
                    c=pre-1
                    while val+v<c:
                        c-=1
                        val+=v
                    pre=c
                else:
                    v-=1
                out+=v
        return out
                