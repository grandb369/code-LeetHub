class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {
        int cur=0;
        for(int i:arr)
        {
            if (i!=cur+1)
            {
                int diff=i-cur-1;
                if(diff>=k)
                {
                    return cur+k;
                }
                k-=diff;
            }
            cur=i;
        }
        return cur+k;
    }
};