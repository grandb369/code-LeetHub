class TextEditor:

    def __init__(self):
        self.stack1=[]
        self.stack2=[]

    def addText(self, text: str) -> None:
        for i in text:
            self.stack1.append(i)

    def deleteText(self, k: int) -> int:
        c=0
        while self.stack1 and k:
            self.stack1.pop()
            k-=1
            c+=1
        return c

    def cursorLeft(self, k: int) -> str:
        while self.stack1 and k:
            self.stack2.append(self.stack1.pop())
            k-=1
        n=len(self.stack1)
        out=''
        for i in range(n-1,n-11,-1):
            if i<0:
                break
            out=self.stack1[i]+out
        return out

    def cursorRight(self, k: int) -> str:
        while self.stack2 and k:
            self.stack1.append(self.stack2.pop())
            k-=1
        n=len(self.stack1)
        out=''
        for i in range(n-1,n-11,-1):
            if i<0:
                break
            out=self.stack1[i]+out
        return out


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)