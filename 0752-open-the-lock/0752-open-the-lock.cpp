class Solution {
public:
    int openLock(vector<string>& deadends, string target) {
        set<string>temp(deadends.begin(),deadends.end());
        if (temp.find("0000")!=temp.end())return -1;
        if(target=="0000")return 0;
        vector<string>stack{"0000"};
        set<string>seen{"0000"};
        string org="0123456789";
        string fo="1234567890";
        string ba="9012345678";
        map<char,char>up;
        map<char,char>down;
        for(int i=0;i<10;i++)
        {
            up[org[i]]=fo[i];
            down[org[i]]=ba[i];
        }
        int out=0;
        while(stack.size()>0)
        {
            out++;
            vector<string>nex;
            for(string cur:stack)
            {
                for(int i=0;i<4;i++)
                {
                    cur[i]=up[cur[i]];
                    if (cur==target)return out;
                    if(temp.find(cur)==temp.end() && seen.find(cur)==seen.end())
                    {
                        nex.push_back(cur);
                        seen.insert(cur);
                    }
                    cur[i]=down[down[cur[i]]];
                    if (cur==target)return out;
                    if(temp.find(cur)==temp.end() && seen.find(cur)==seen.end())
                    {
                        nex.push_back(cur);
                        seen.insert(cur);
                    }
                    cur[i]=up[cur[i]];
                }
            }
            stack=nex;
        }
        return -1;
    }
};