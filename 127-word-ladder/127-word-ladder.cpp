#include<stdio.h>
#include <arpa/inet.h>
#include<stdlib.h>
class Solution {
public:
    int ladderLength(string start, string end, vector<string>& words) {
        map<string,set<string>>graph;
        for(string w:words)
        {
            for(int i=0;i<w.size();i++)
            {
                string s=w;
                s[i]='#';
                graph[s].insert(w);
            }
        }
        int out=1;
        set<string>seen{start};
        vector<string>stack{start};
        while(stack.size()>0)
        {
            out++;
            vector<string>nex;
            for(string w:stack)
            {
                for(int i=0;i<w.size();i++)
                {
                    string s=w;
                    s[i]='#';
                    for(string ss:graph[s])
                    {
                        if(ss==end)return out;
                        if(seen.find(ss)==seen.end())
                        {
                            seen.insert(ss);
                            nex.push_back(ss);
                        }
                    }
                }
            }
            stack=nex;
        }
        return 0;
    }
};