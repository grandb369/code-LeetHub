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
        mi=min(10,n)
        return ''.join(self.stack1[n-mi:n])

    def cursorRight(self, k: int) -> str:
        while self.stack2 and k:
            self.stack1.append(self.stack2.pop())
            k-=1
        n=len(self.stack1)
        mi=min(10,n)
        return ''.join(self.stack1[n-mi:n])


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)