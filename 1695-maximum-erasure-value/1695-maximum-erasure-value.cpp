class Solution {
public:
    int maximumUniqueSubarray(vector<int>& nums) {
        int out=0;
        int val=0;
        set<int>temp;
        int i=0;
        int pre=0;
        int n=nums.size();
        while(i<n)
        {
            if(temp.find(nums[i])==temp.end())
            {
                temp.insert(nums[i]);
                val+=nums[i];
                i++;
            }
            else
            {
                out=max(out,val);
                while(nums[pre]!=nums[i])
                {
                    val-=nums[pre];
                    temp.erase(nums[pre]);
                    pre++;
                    
                }
                val-=nums[pre];
                temp.erase(nums[pre]);
                pre++;
            }
        }
        return max(out,val);
    }
};