class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i in '+-*/':
                b=stack.pop()
                f=stack.pop()
                if i=='+':
                    val=b+f
                elif i=='-':
                    val=f-b
                elif i=='*':
                    val=f*b
                else:
                    neg=True
                    if f*b>=0:
                        neg=False
                    val=abs(f)//abs(b)
                    if neg:
                        val*=-1
                stack.append(val)
            else:
                stack.append(int(i))
        return stack[0]