class Solution:
    def checkValidString(self, s: str) -> bool:
        star=0
        stack=[]
        for i in s:
            if i=='*':
                star+=1
            elif i=='(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                elif star:
                    star-=1
                else:
                    return False
        if len(stack)>star:
            return False
        stack=[]
        star=0
        k={'(':')',')':'(','*':'*'}
        for i in [k[i]for i in s][::-1]:
            if i=='*':
                star+=1
            elif i=='(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                elif star:
                    star-=1
                else:
                    return False
        if len(stack)>star:
            return False
        return True