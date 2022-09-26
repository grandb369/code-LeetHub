class Solution {
public:
    int find(vector<int>& data, int x)
    {
        if(x!=data[x])
        {
            data[x]=find(data,data[x]);
        }
        return data[x];
    }
    bool u(vector<int>& data, int x, int y)
    {
        x=find(data,x);
        y=find(data,y);
        if(x==y)return false;
        data[x]=y;
        return true;
    }
    
    bool check(vector<int>& data, int x, int y)
    {
        x=find(data,x);
        y=find(data,y);
        if(x==y)return true;
        return false;
    }
    
    bool equationsPossible(vector<string>& nums) {
        vector<int>data(26);
        for(int i=0;i<26;i++)data[i]=i;
        for(string cur:nums)
        {
            if(cur[1]=='=')
            {
                bool val=u(data,cur[0]-'a',cur[3]-'a');
            }
        }
        for(string cur:nums)
        {
            if(cur[1]=='!')
            {
                if(check(data,cur[0]-'a',cur[3]-'a'))return false;
            }
        }
        return true;
    }
};