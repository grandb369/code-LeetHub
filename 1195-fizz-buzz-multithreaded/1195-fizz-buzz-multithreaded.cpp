class FizzBuzz {
private:
    mutex fi,bu,num,fibu;
    int n;

public:
    FizzBuzz(int n) {
        this->n = n+1;
        this->fi.lock();
        this->bu.lock();
        this->fibu.lock();
    }

    // printFizz() outputs "fizz".
    void fizz(function<void()> printFizz) {
        for(int i=1;i<this->n;i++)
        {
            if(i%3==0 && i%5!=0)
            {
                this->fi.lock();
                printFizz();
                this->num.unlock();
            }
        }
    }

    // printBuzz() outputs "buzz".
    void buzz(function<void()> printBuzz) {
        for(int i=1;i<this->n;i++)
        {
            if(i%3!=0 && i%5==0)
            {
                this->bu.lock();
                printBuzz();
                this->num.unlock();
            }
        }
    }

    // printFizzBuzz() outputs "fizzbuzz".
	void fizzbuzz(function<void()> printFizzBuzz) {
        for(int i=1;i<this->n;i++)
        {
            if(i%3==0 && i%5==0)
            {
                this->fibu.lock();
                printFizzBuzz();
                this->num.unlock();
            }
        }
    }

    // printNumber(x) outputs "x", where x is an integer.
    void number(function<void(int)> printNumber) {
        for(int i=1;i<this->n;i++)
        {
            this->num.lock();
            if(i%3==0 && i%5==0)
            {
                this->fibu.unlock();
            }
            else if(i%3==0)
            {
                this->fi.unlock();
            }
            else if(i%5==0)
            {
                this->bu.unlock();
            }
            else
            {
                printNumber(i);
                this->num.unlock();
            }
        }
    }
};