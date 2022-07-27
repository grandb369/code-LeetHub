class MaxStack {
public:
    vector<int>data;
    map<int,vector<int>>ma;
    set<int>del;
    MaxStack() {
        
    }
    
    void push(int x) {
        data.push_back(x);
        ma[x].push_back(data.size()-1);
    }
    
    int pop() {
        int n=data.size()-1;
        int val=data.back();
        data.pop_back();
        ma[val].pop_back();
        if(ma[val].size()==0)
        {
            ma.erase(val);
        }
        n--;
        while(del.find(n)!=del.end())
        {
            data.pop_back();
            del.erase(n);
            n--;
        }
        return val;
    }
    
    int top() {
        return data.back();
    }
    
    int peekMax() {
        return data[ma.rbegin()->second.back()];
    }
    
    int popMax() {
        int index=ma.rbegin()->second.back();
        ma.rbegin()->second.pop_back();
        if(ma.rbegin()->second.size()==0)
        {
            ma.erase(ma.rbegin()->first);
        }
        if(index+1==data.size())
        {
            int val=data.back();
            data.pop_back();
            int n=data.size()-1;
            while(del.find(n)!=del.end())
            {
                data.pop_back();
                del.erase(n);
                n--;
            }
            return val;
        }
        del.insert(index);
        return data[index];
    }
};

/**
 * Your MaxStack object will be instantiated and called as such:
 * MaxStack* obj = new MaxStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->peekMax();
 * int param_5 = obj->popMax();
 */