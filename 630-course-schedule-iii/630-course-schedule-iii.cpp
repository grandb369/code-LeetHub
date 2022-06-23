class Solution {
public:
    int scheduleCourse(vector<vector<int>>& nums) {
        priority_queue<int>temp;
        int time=0;
        sort(nums.begin(),nums.end(),[](const vector<int>&a, const vector<int>&b){
            return a[1]<b[1];
        });
        for(auto i:nums)
        {
            int t=i[0];
            int end=i[1];
            temp.push(t);
            time+=t;
            while(time>end)
            {
                int last=temp.top();
                temp.pop();
                time-=last;
            }
        }
        return temp.size();
    }
};