class Solution {
public:
    double average(vector<int>& salary) {
        int l=pow(10,6);
        int r= 0;
        long su=0;
        for(int i:salary)
        {
            su+=i;
            l=min(l,i);
            r=max(r,i);
        }
        return (double)(su-l-r)/(salary.size()-2);
    }
};