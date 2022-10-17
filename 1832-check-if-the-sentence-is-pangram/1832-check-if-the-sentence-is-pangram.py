class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        temp=set([chr(i)for i in range(97,123)])
        for i in sentence:
            if i in temp:
                temp.remove(i)
        return len(temp)==0