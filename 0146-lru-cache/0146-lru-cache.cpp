struct node{
    int key;
    int val;
    node* next;
    node* prev;
    node():key(-1),val(-1),next(nullptr),prev(nullptr){};
    node(int k, int v):key(k),val(v),next(nullptr),prev(nullptr){};
};
class LRUCache {
public:
    int n;
    map<int,node*>data;
    node* head;
    node* tail;
    
    LRUCache(int c) {
        n=c;
        head=new node();
        tail=new node();
        head->next=tail;
        tail->prev=head;
    }
    
    int get(int key) {
        if(data.find(key)==data.end())return -1;
        int val=data[key]->val;
        remove(key);
        add(key,val);
        return data[key]->val;
        
    }
    
    void put(int key, int value) {
        remove(key);
        if(n==0)pop();
        add(key,value);
    }
    
    void pop()
    {
        if(n==0)
        {
            node* pre=tail->prev->prev;
            node* cur=pre->next;
            pre->next=tail;
            tail->prev=pre;
            n++;
            data.erase(cur->key);
        }
    }
    
    void remove(int key)
    {
        if (data.find(key)!=data.end())
        {
            node* cur=data[key];
            node* pre=cur->prev;
            node* nex=cur->next;
            pre->next=nex;
            nex->prev=pre;
            n++;
            data.erase(cur->key);
        }
    }
    
    void add(int key, int value)
    {
        if(data.find(key)==data.end())
        {
            node*cur = new node(key,value);
            node *nex=head->next;
            head->next=cur;
            cur->next=nex;
            nex->prev=cur;
            cur->prev=head;
            n--;
            data[key]=cur;
        }
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */