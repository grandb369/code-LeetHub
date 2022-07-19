class Solution {
public:
    vector<int> asteroidCollision(vector<int>& nums) {
        vector<int>out;
        for(int i:nums)
        {
            while(i<0 && out.size()>0 and out.back()>0)
            {
                int val=out.back();
                out.pop_back();
                if(val>-i)
                {
                    i=val;
                    break;
                }
                else if(val==-i)
                {
                    i=0;
                }
            }
            if(i!=0)out.push_back(i);
        }
        return out;
    }
};