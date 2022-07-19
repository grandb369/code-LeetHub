struct node{
    int key;
    int val;
    int fre;
    node* next;
    node* prev;
    node():key(-1),val(-1),fre(0){};
    node(int k, int v):key(k),val(v),fre(1){};
};

struct level{
    node* head;
    node* tail;
    int n;
    int fre;
    map<int,node*>data;
    level(int f){
        head=new node();
        tail=new node();
        head->next=tail;
        tail->next=head;
        n=0;
        fre=f;
    }
    
    node* remove(int key)
    {
        if(data.find(key)==data.end())return nullptr;
        node* cur=data[key];
        node* pre=cur->prev;
        node* nex=cur->next;
        pre->next=nex;
        nex->prev=pre;
        n--;
        data.erase(key);
        return cur;
    }
    
    node* pop()
    {
        if(n==0)return nullptr;
        return remove(tail->prev->key);
    }
    
    void add(node* root)
    {
        node* nex=head->next;
        head->next=root;
        root->next=nex;
        nex->prev=root;
        root->prev=head;
        n++;
        data[root->key]=root;
    }
};

class LFUCache {
public:
    map<int,level*>fres;
    int n;
    int c;
    int min_fre;
    map<int,node*>nodes;
    LFUCache(int ca) {
        n=ca;
        c=ca;
        min_fre=1;
    }
    
    void update(node* cur){
        int f=cur->fre;
        level* cur_lev=fres[f];
        cur=cur_lev->remove(cur->key);
        if (cur_lev->n==0)
        {
            fres.erase(f);
            if(min_fre==f)min_fre++;
        }
        cur->fre++;
        f=cur->fre;
        if(fres.find(f)==fres.end())
        {
            fres[f]=new level(f);
        }
        cur_lev=fres[f];
        cur_lev->add(cur);
        nodes[cur->key]=cur;
    }
    
    int get(int key) {
        if(nodes.find(key)==nodes.end())return -1;
        node* cur=nodes[key];
        update(cur);
        return cur->val;
    }
    
    void put(int key, int value) {
        if(c==0)return;
        if(nodes.find(key)!=nodes.end())
        {
            node* cur=nodes[key];
            cur->val=value;
            update(cur);
            nodes[key]=cur;
        }
        else
        {
            if(n==0)
            {
                level* min_lev=fres[min_fre];
                node* cur = min_lev->pop();
                if(min_lev->n==0)
                {
                    fres.erase(min_fre);
                    min_fre++;
                }
                nodes.erase(cur->key);
                n++;
            }
            node* cur = new node(key, value);
            if(fres.find(1)==fres.end())
            {
                fres[1]=new level(1);
            }
            fres[1]->add(cur);
            min_fre=1;
            nodes[key]=cur;
            n--;
        }
    }
};

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache* obj = new LFUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */