struct node{
    int val;
    node* next;
    node* pre;
    node():val(0),next(nullptr){};
    node(int v):val(v),next(nullptr){};
};
class MyLinkedList {
public:
    node* head;
    node* tail;
    int n;
    MyLinkedList() {
        head=new node();
        tail=new node();
        head->next=tail;
        tail->pre=head;
        n=0;
    }
    
    int get(int index) {
        if(index>=n)return -1;
        node* cur=head->next;
        while(index>0)
        {
            cur=cur->next;
            index--;
        }
        return cur->val;
    }
    
    void addAtHead(int val) {
        node* nex=head->next;
        node* cur=new node(val);
        head->next=cur;
        cur->next=nex;
        nex->pre=cur;
        cur->pre=head;
        n++;
    }
    
    void addAtTail(int val) {
        node* pre=tail->pre;
        node* cur=new node(val);
        pre->next=cur;
        cur->next=tail;
        tail->pre=cur;
        cur->pre=pre;
        n++;
    }
    
    void addAtIndex(int index, int val) {
        if(index<=n)
        {
            node* pre=head;
            while(index>0)
            {
                pre=pre->next;
                index--;
            }
            node* nex=pre->next;
            node* cur=new node(val);
            pre->next=cur;
            cur->next=nex;
            nex->pre=cur;
            cur->pre=pre;
            n++;
        }

    }
    
    void deleteAtIndex(int index) {
        if(index<n)
        {
            node* pre=head;
            while(index>0)
            {
                pre=pre->next;
                index--;
            }
            node* nex=pre->next->next;
            pre->next=nex;
            nex->pre=pre;
            n--;
        }
    }
    
};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */