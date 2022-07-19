class Solution {
public:
    vector<int> findOrder(int n, vector<vector<int>>& pre) {
        vector<int>count(n,0);
        map<int,vector<int>>unlock;
        for(vector<int> c:pre)
        {
            count[c[0]]++;
            unlock[c[1]].push_back(c[0]);
        }
        int len=n;
        vector<int>stack;
        for(int i=0;i<len;i++)
        {
            if(count[i]==0)
            {
                stack.push_back(i);
                n--;
            }
        }
        vector<int>out;
        while(stack.size())
        {
            vector<int>temp;
            for(int cur:stack)
            {
                out.push_back(cur);
                for(int nex:unlock[cur])
                {
                    count[nex]--;
                    if(count[nex]==0)
                    {
                        temp.push_back(nex);
                        n--;
                    }
                }
            }
            stack=temp;
        }
        return n==0?out:vector<int>{};
    }
};