import threading
class Foo:
    def __init__(self):
        self.p1=threading.Event()
        self.p2=threading.Event()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.p1.set()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.p1.wait()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.p1.clear()
        self.p2.set()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.p2.wait()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
        self.p2.clear()