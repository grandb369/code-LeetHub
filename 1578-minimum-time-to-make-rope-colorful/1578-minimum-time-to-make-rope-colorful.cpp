class Solution {
public:
    int minCost(string col, vector<int>& nums) {
        priority_queue<int, std::vector<int>, std::greater<int>> temp;
        int out=0;
        char pre='#';
        for(int i=0;i<col.size();i++)
        {
            if(pre!=col[i])
            {
                while(temp.size()>1)
                {
                    out+=temp.top();
                    temp.pop();
                }
                temp=priority_queue<int, std::vector<int>, std::greater<int>>();
            }
            temp.push(nums[i]);
            pre=col[i];
        }
        while(temp.size()>1)
        {
            out+=temp.top();
            temp.pop();
        }
        return out;
    }
};