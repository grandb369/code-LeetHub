class Solution {
public:
    int maxArea(int h, int w, vector<int>& hor, vector<int>& ver) {
        int max_h=0,max_v=0;
        sort(hor.begin(),hor.end());
        sort(ver.begin(),ver.end());
        hor.push_back(h);
        ver.push_back(w);
        int pre=0;
        int mod=(int)pow(10,9)+7;
        for(int i=0;i<hor.size();i++)
        {
            max_h=max(max_h,hor[i]-pre);
            pre=hor[i];
        }
        pre=0;
        for(int i=0;i<ver.size();i++)
        {
            max_v=max(max_v,ver[i]-pre);
            pre=ver[i];
        }
        max_h%=mod;
        max_v%=mod;
        long long out=((long long)max_h*max_v)%mod;
        return out;
    }
};