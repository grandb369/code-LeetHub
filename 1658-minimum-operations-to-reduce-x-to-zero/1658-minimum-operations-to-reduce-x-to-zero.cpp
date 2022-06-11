class Solution {
public:
    int minOperations(vector<int>& nums, int x) {
        int val=0;
        int i=0;
        int n=nums.size();
        int out=n+1;
        int count=0;
        while (i<n && val<x)
        {
            val+=nums[i];
            i++;
            count++;
        }
        if(val==x)out=min(out,count);
        if(val<x)return -1;
        if(i>=n && val!=x)return -1;
        int j=n-1;
        i--;
        while (i>=0)
        {
            val-=nums[i];
            i--;
            count--;
            while(j>i && val<x)
            {
                val+=nums[j];
                j--;
                count++;
            }
            if(val==x)out=min(out,count);
        }
        return out!=n+1?out:-1;
    }
};