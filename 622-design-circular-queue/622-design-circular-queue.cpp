struct Node{
    int val;
    Node* nex;
    Node* pre;
    Node(int v):val(v){};
};
class MyCircularQueue {
public:
    int c;
    int len;
    Node* head;
    MyCircularQueue(int k) {
        c=k;
        len=0;
        head=new Node(0);
        head->nex=head;
        head->pre=head;
    }
    
    bool enQueue(int value) {
        if(len==c)return false;
        len++;
        Node* root= new Node(value);
        Node* pre = head->pre;
        pre->nex=root;
        root->nex=head;
        
        head->pre=root;
        root->pre=pre;
        return true;
    }
    
    bool deQueue() {
        if (len==0)return false;
        Node* nex= head->nex->nex;
        head->nex=nex;
        nex->pre=head;
        len--;
        return true;
    }
    
    int Front() {
        return len==0?-1:head->nex->val;
    }
    
    int Rear() {
        return len==0?-1:head->pre->val;
    }
    
    bool isEmpty() {
        return len==0;
    }
    
    bool isFull() {
        return len==c;
    }
};

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue* obj = new MyCircularQueue(k);
 * bool param_1 = obj->enQueue(value);
 * bool param_2 = obj->deQueue();
 * int param_3 = obj->Front();
 * int param_4 = obj->Rear();
 * bool param_5 = obj->isEmpty();
 * bool param_6 = obj->isFull();
 */