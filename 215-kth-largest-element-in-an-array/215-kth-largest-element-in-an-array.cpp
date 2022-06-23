class Solution {
public:
    void qs(vector<int>& nums, int l, int r)
    {
        if(l<r)
        {
            int point=nums[r];
            int j=r-1;
            int i=l;
            while(i<j)
            {
                while(i<j && nums[i]<point)
                {
                    i++;
                }
                while(i<j && nums[j]>=point)
                {
                    j--;
                }
                if(i<j)
                {
                    int temp=nums[i];
                    nums[i]=nums[j];
                    nums[j]=temp;
                }
            }
            if (nums[i]>=point)
            {
                int temp=nums[i];
                nums[i]=point;
                nums[r]=temp;
            }
            qs(nums,l,i);
            qs(nums,i+1,r);
        }
    }
    int findKthLargest(vector<int>& nums, int k) {
        qs(nums,0,nums.size()-1);
        return nums[nums.size()-k];
    }
};