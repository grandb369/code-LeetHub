class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i=='(':
                stack.append(')')
            elif i=='[':
                stack.append(']')
            elif i=='{':
                stack.append('}')
            else:
                if not stack or stack[-1]!=i:
                    return False
                stack.pop()
        return len(stack)==0