class ZeroEvenOdd {
private:
    int n;
    mutex m0,mo,me;

public:
    ZeroEvenOdd(int n) {
        this->n = n;
        me.lock();
        mo.lock();
    }

    // printNumber(x) outputs "x", where x is an integer.
    void zero(function<void(int)> printNumber) {
        for(int i=1;i<this->n+1;i++)
        {
            m0.lock();
            printNumber(0);
            if (i%2)
            {
                mo.unlock();
            }
            else
            {
                me.unlock();
            }
        }
            
        
    }

    void even(function<void(int)> printNumber) {
        for(int i=1;i<this->n+1;i++)
        {
            if(i%2)continue;
            me.lock();
            printNumber(i);
            m0.unlock();
        }
    }

    void odd(function<void(int)> printNumber) {
        for(int i=1;i<this->n+1;i++)
        {
            if(i%2==0)continue;
            mo.lock();
            printNumber(i);
            m0.unlock();
        }
    }
};