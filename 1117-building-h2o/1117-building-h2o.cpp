class H2O {
public:
    mutex m1,m2;
    int h;
    H2O() {
        h=0;
        m2.lock();
    }

    void hydrogen(function<void()> releaseHydrogen) {
        m1.lock();
        h++;
        // releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen();
        if(h==2)
        {
            h=0;
            m2.unlock();
        }
        else
        {
            m1.unlock();
        }
    }

    void oxygen(function<void()> releaseOxygen) {
        m2.lock();
        // releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen();
        m1.unlock();
    }
};