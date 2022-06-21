import threading
class Foo:
    def __init__(self):
        self.p1=threading.Lock()
        self.p2=threading.Lock()
        self.p1.acquire()
        self.p2.acquire()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.p1.release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.p1.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.p2.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.p2.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()