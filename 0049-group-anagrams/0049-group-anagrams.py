class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        k=collections.defaultdict(list)
        for i in strs:
            k[''.join(sorted(i))].append(i)
        out=[]
        for i in k:
            out.append(k[i])
        return out