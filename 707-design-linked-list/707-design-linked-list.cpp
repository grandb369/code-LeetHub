struct node{
    int val;
    node* next;
    node():val(0),next(nullptr){};
    node(int v):val(v),next(nullptr){};
};
class MyLinkedList {
public:
    node* head;
    int n;
    MyLinkedList() {
        head=new node();
        n=0;
    }
    
    int get(int index) {
        if (index>=n)return -1;
        node* cur=head->next;
        while(index>0)
        {
            cur=cur->next;
            index--;
        }
        return cur->val;
        
    }
    
    void addAtHead(int val) {
        node* cur=new node(val);
        node* nex=head->next;
        head->next=cur;
        cur->next=nex;
        n++;
    }
    
    void addAtTail(int val) {
        node* nex=new node(val);
        node* cur=head;
        while(cur->next!=nullptr)
        {
            cur=cur->next;
        }
        cur->next=nex;
        n++;
    }
    
    void addAtIndex(int index, int val) {
        if(index<=n)
        {
            node* pre=head;
            while(index>0)
            {
                index--;
                pre=pre->next;
            }
            node* nex=pre->next;
            node* cur = new node(val);
            pre->next=cur;
            cur->next=nex;
            n++;
        }
    }
    
    void deleteAtIndex(int index) {
        if(index<n)
        {
            node* pre=head;
            while (index>0)
            {
                index--;
                pre=pre->next;
            }
            node* nex=pre->next->next;
            pre->next=nex;
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