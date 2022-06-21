from threading import Lock, Event
class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.m0=Lock()
        self.m1=Lock()
        self.m2=Lock()
        self.m1.acquire()
        self.m2.acquire()
        
        
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, 1+self.n):
            self.m0.acquire()
            printNumber(0)
            if i%2:
                self.m1.release()
            else:
                self.m2.release()
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for j in range(2,1+self.n,2):
            self.m2.acquire()
            printNumber(j)
            self.m0.release()
        
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for x in range(1,1+self.n,2):
            self.m1.acquire()
            printNumber(x)
            self.m0.release()
        