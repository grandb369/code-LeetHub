class MyCalendarThree {
public:
    map<int,int>data;
    MyCalendarThree() {
        
    }
    
    int book(int start, int end) {
        data[start]++;
        data[end]--;
        int out=0;
        int cur=0;
        for(auto lt=data.begin();lt!=data.end();lt++)
        {
            cur+=lt->second;
            out=max(out,cur);
        }
        return out;
    }
};

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * MyCalendarThree* obj = new MyCalendarThree();
 * int param_1 = obj->book(start,end);
 */