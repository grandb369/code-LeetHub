class Solution:
    def simplifyPath(self, path: str) -> str:
        out=''
        s=path.replace('//','/')
        s=s.split('/')
        stack=[]
        for i in s:
            if i:
                if i=='..':
                    if stack:
                        stack.pop()
                elif i!='.':
                    stack.append(i)
        out='/'+'/'.join(stack)
        return out