class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        out=[0 for i in range(len(deck))]
        temp=[i for i in range(len(deck))]
        i=0
        while temp:
            i=i%len(temp)
            ind=temp.pop(i)
            out[ind]=deck.pop()
            i+=1
        return out
        