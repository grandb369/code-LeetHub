class Solution {
public:
    int countPrimes(int n) {
        vector<bool>temp(n+1,true);
        int out=0;
        for(int i=2;i<n;i++)
        {
            if(temp[i])
            {
                out++;
                int v=i;
                while (v<=n)
                {
                    temp[v]=false;
                    v+=i;
                }
            }
        }
        return out;
    }
};