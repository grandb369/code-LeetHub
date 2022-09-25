class Node:
    def __init__(self,val=0):
        self.val=val
        self.nex=None
        self.pre=None
        
class MyCircularQueue:

    def __init__(self, k: int):
        self.len=0
        self.k=k
        self.head=Node()
        self.head.nex=self.head.pre=self.head

    def enQueue(self, value: int) -> bool:
        if self.len==self.k:
            return False
        pre=self.head.pre
        root=Node(value)
        
        pre.nex=root
        root.nex=self.head
        
        self.head.pre=root
        root.pre=self.head
        self.len+=1
        return True

    def deQueue(self) -> bool:
        if self.len==0:
            return False
        nex=self.head.nex.nex
        self.head.nex=nex
        nex.pre=self.head
        self.len-=1
        return True

    def Front(self) -> int:
        if self.len==0:
            return -1
        return self.head.nex.val

    def Rear(self) -> int:
        if self.len==0:
            return -1
        return self.head.pre.val

    def isEmpty(self) -> bool:
        return self.len==0

    def isFull(self) -> bool:
        return self.len==self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()