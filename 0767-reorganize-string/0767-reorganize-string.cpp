#include <queue>
class Solution {
public:
    string reorganizeString(string s) {
        map<char,int>temp;
        int n=(s.size()+1)/2;
        for(char c:s){
            temp[c]++;
            if(temp[c]>n)return "";
        }
        std::priority_queue<std::pair<int, char>> q;
        for(auto cur=temp.begin();cur!=temp.end();cur++){
            q.push({cur->second, cur->first});
        }
        string out="";
        while(q.size()){
            auto cur=q.top();
            q.pop();
            if(out.size()>0 && out[out.size()-1]==cur.second){
                auto sec=q.top();
                q.pop();
                out+=sec.second;
                if(sec.first>1){
                    q.push({sec.first-1,sec.second});
                }
            }
            else{
                out+=cur.second;
                cur.first--;
            }
            if(cur.first>0){
                q.push({cur.first,cur.second});
            }
        }
        return out;
    }
};