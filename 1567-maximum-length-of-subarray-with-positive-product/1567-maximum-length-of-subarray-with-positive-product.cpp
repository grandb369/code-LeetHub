class Solution {
public:
    int getMaxLen(vector<int>& nums) {
        for(int i=0;i<nums.size();i++)
        {
            nums[i]=nums[i]==0?0:(nums[i]>0?1:-1);
        }
        int ma=1;
        int mi=1;
        int cma=0;
        int cmi=0;
        int out=0;
        for(int i:nums)
        {
            int temp_ma = ma*i;
            int temp_mi = mi*i;
            if (temp_ma>temp_mi)
            {
                ma=temp_ma;
                mi=temp_mi;
                cma++;
                cmi++;
            }
            else if (temp_ma<temp_mi)
            {
                ma=temp_mi;
                mi=temp_ma;
                int temp=cmi+1;
                cmi=cma+1;
                cma=temp;
            }
            else
            {
                ma=temp_mi;
                mi=temp_mi;
                cmi=max(cmi,cma)+1;
                cma=cmi;
            }
            if(i>ma)
            {
                ma=i;
                cma=1;
            }
            if (i<mi)
            {
                mi=i;
                cmi=1;
            }
            if (ma>0)
            {
                out=max(out,cma);
            }
            
        }
        return out;
    }
};