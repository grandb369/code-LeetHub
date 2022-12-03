class Solution {
public:
    string frequencySort(string s) {
        map<char,int>temp;
        for(char c:s)temp[c]++;
        map<int,vector<char>>temp2;
        for(auto lt:temp)
        {
            temp2[lt.second].push_back(lt.first);
        }
        string out="";
        for(auto lt:temp2){
            for(char c:lt.second){
                out+=string(lt.first,c);
            }
        }
        reverse(out.begin(),out.end());
        return out;
    }
};