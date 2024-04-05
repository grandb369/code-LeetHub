class Solution:
    def makeGood(self, s: str) -> str:
        stack=[]
        for i in s:
            if i==i.upper():
                if stack and stack[-1]==i.lower():
                    stack.pop()
                else:
                    stack.append(i)
            else:
                if stack and stack[-1]==i.upper():
                    stack.pop()
                else:
                    stack.append(i)
        return ''.join(stack)