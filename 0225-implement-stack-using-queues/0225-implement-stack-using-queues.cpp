class MyStack {
public:
    vector<int>stack;
    MyStack() {
        
    }
    
    void push(int x) {
        stack.push_back(x);
    }
    
    int pop() {
        int val=top();
        stack.pop_back();
        return val;
    }
    
    int top() {
        return stack.back();
    }
    
    bool empty() {
        return stack.size()==0;
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */