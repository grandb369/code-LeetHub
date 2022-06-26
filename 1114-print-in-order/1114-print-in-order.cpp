#include <semaphore.h>
class Foo {
public:
    sem_t p1;
    sem_t p2;
    Foo() {
        sem_init(&p1,0,0);
        sem_init(&p2,0,0);
        
    }

    void first(function<void()> printFirst) {
        
        // printFirst() outputs "first". Do not change or remove this line.
        printFirst();
        sem_post(&p1);
    }

    void second(function<void()> printSecond) {
        sem_wait(&p1);
        // printSecond() outputs "second". Do not change or remove this line.
        printSecond();
        sem_post(&p2);
    }

    void third(function<void()> printThird) {
        sem_wait(&p2);
        // printThird() outputs "third". Do not change or remove this line.
        printThird();
    }
};