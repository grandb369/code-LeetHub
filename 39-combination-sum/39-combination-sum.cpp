class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& nums, int t) {
        sort(nums.begin(),nums.end());
        vector<vector<int>>stack;
        vector<vector<int>>out;
        vector<int>ind;
        vector<int>val;
        int n=nums.size();
        int i,j;
        int c=0;
        for(int v:nums)
        {
            vector<int>temp{v};
            if(v==t)
            {
                out.push_back(temp);
                continue;
            }
            stack.push_back(temp);
            val.push_back(v);
            ind.push_back(c);
            c++;
        }
        while(stack.size()>0)
        {
            vector<vector<int>>stack2;
            vector<int>val2;
            vector<int>ind2;
            vector<int>temp;
            for(i=0;i<stack.size();i++)
            {
                vector<int>cur=stack[i];
                int v=val[i];
                int index=ind[i];
                for(j=index;j<n;j++)
                {
                    if(v+nums[j]==t)
                    {
                        cur.push_back(nums[j]);
                        out.push_back(cur);
                        break;
                    }
                    else if(v+nums[j]<t)
                    {
                        vector<int>nex=cur;
                        nex.push_back(nums[j]);
                        stack2.push_back(nex);
                        val2.push_back(v+nums[j]);
                        ind2.push_back(j);
                    }
                }
            }
            stack=stack2;
            val=val2;
            ind=ind2;
        }
        return out;
    }
};