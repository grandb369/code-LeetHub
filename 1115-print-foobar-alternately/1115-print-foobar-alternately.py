import threading
class FooBar:
    def __init__(self, n):
        self.n = n
        self.lock_foo = threading.Event()
        self.lock_bar = threading.Event()
        self.lock_foo.set()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.lock_foo.wait()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.lock_foo.clear()
            self.lock_bar.set()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.lock_bar.wait()    
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.lock_bar.clear()
            self.lock_foo.set()
            