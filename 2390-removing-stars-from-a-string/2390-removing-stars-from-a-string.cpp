class Solution {
public:
    string removeStars(string s) {
        vector<char>temp;
        for(char c:s){
            if(c=='*'){
                if(temp.size()>0){
                    temp.pop_back();
                }
            }
            else{
                temp.push_back(c);
            }
        }
        string out;
        for(char c:temp){
            out+=c;
        }
        return out;
    }
};