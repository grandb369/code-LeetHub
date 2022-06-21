from threading import Lock
class H2O:
    def __init__(self):
        self.l1=Lock()
        self.l2=Lock()
        self.h=0
        self.l2.acquire()


    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.l1.acquire()
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        self.h+=1
        if self.h==2:
            self.h=0
            self.l2.release()
        else:
            self.l1.release()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.l2.acquire()
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        self.l1.release()