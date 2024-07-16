class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        map<int,int> k;
        for(int i:nums1)
        {
            if(k.find(i)==k.end())
            {
                k[i]=0;
            }
            k[i]++;
        }
        vector<int>out;
        for (int i:nums2)
        {
            if(k.find(i)!=k.end() && k[i]!=0)
            {
                out.push_back(i);
                k[i]--;
            }
        }
        return out;
    }
};