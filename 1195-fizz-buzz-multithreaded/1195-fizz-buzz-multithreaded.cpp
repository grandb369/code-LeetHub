class FizzBuzz {
private:
    mutex fi,bu,num,fibu;
    int n;

public:
    FizzBuzz(int n) {
        this->n = n+1;
        fi.lock();
        bu.lock();
        fibu.lock();
    }

    // printFizz() outputs "fizz".
    void fizz(function<void()> printFizz) {
        for(int i=1;i<this->n;i++)
        {
            if(i%3==0 && i%5!=0)
            {
                fi.lock();
                printFizz();
                num.unlock();
            }
        }
    }

    // printBuzz() outputs "buzz".
    void buzz(function<void()> printBuzz) {
        for(int i=1;i<this->n;i++)
        {
            if(i%3!=0 && i%5==0)
            {
                bu.lock();
                printBuzz();
                num.unlock();
            }
        }
    }

    // printFizzBuzz() outputs "fizzbuzz".
	void fizzbuzz(function<void()> printFizzBuzz) {
        for(int i=1;i<this->n;i++)
        {
            if(i%3==0 && i%5==0)
            {
                fibu.lock();
                printFizzBuzz();
                num.unlock();
            }
        }
    }

    // printNumber(x) outputs "x", where x is an integer.
    void number(function<void(int)> printNumber) {
        for(int i=1;i<this->n;i++)
        {
            num.lock();
            if(i%3==0 && i%5==0)
            {
                fibu.unlock();
            }
            else if(i%3==0)
            {
                fi.unlock();
            }
            else if(i%5==0)
            {
                bu.unlock();
            }
            else
            {
                printNumber(i);
                num.unlock();
            }
        }
    }
};