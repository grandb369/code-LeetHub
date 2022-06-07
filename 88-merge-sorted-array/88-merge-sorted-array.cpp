class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        if (m==0)
        {
            nums1=nums2;
        }
        else if(n!=0)
        {
            int cur=nums1.size()-1;
            int p1=m-1;
            int p2=n-1;
            while(n>0)
            {
                if (p1>=0 && nums1[p1]>nums2[p2])
                {
                    int temp=nums1[p1];
                    nums1[p1]=nums1[cur];
                    nums1[cur]=temp;
                    p1--;
                }
                else
                {
                    nums1[cur]=nums2[p2];
                    p2--;
                    n--;
                }
                cur--;
            }
        }
    }
};