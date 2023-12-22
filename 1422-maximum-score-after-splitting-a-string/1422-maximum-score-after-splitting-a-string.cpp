class Solution {
public:
    int maxScore(string s) {
        int z=0;
        int o=0;
        int out=0;
        int n=s.size();
        for(char c:s){
            if(c=='1')o++;
        }
        for(char c:s){
            if(--n==0)break;
            if(c=='1')o--;
            else z++;
            out=max(out,z+o);
        }
        return out;
    }
};