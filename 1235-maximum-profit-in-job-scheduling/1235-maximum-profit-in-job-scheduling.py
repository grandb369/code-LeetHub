class Solution:
    def jobScheduling(self, s: List[int], e: List[int], p: List[int]) -> int:
        nums=set([])
        k=collections.defaultdict(list)
        for i in range(len(s)):
            k[s[i]].append((e[i],p[i]))
            nums.add(s[i])
            nums.add(e[i])
        out=0
        nums=sorted(nums)
        temp=collections.defaultdict(list)
        for i in range(len(nums)):
            i=nums[i]
            for v in temp[i]:
                out=max(v,out)
            for j,v in k[i]:
                temp[j].append(out+v)
        return out