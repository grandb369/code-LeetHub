class Solution {
public:
    bool isPossible(vector<int>& target) {
        priority_queue<long>temp;
        long long su=0;
        for(long i: target)
        {
            temp.push(i);
            su+=i;
        }
        while (true)
        {
            long val=temp.top();
            temp.pop();
            su-=val;
            if(val==1 || su==1)return true;
            if(su>val || su==0 || val%su==0)return false;
            val%=su;
            su+=val;
            temp.push(val);
        }
    }
};