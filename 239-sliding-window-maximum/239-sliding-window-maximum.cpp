class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        deque<int> q;
        int n=nums.size();
        for(int i=0;i<k;i++)
        {
            while(q.size()!=0 && q.back()<nums[i])
            {
                q.pop_back();
            }
            q.push_back(nums[i]);
        }
        vector<int> out;
        out.push_back(q.front());
        for(int i=k;i<n;i++)
        {
            if(q.size()!=0 && q.front()==nums[i-k])
            {
                q.pop_front();
            }
            while(q.size()!=0 && q.back()<nums[i])
            {
                q.pop_back();
            }
            q.push_back(nums[i]);
            out.push_back(q.front());
        }
        return out;
    }
};