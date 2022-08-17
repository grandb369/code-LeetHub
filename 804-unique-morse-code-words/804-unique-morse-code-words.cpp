class Solution {
public:
    int uniqueMorseRepresentations(vector<string>& words) {
                vector<string>code{".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
        set<string>out;
        for(auto s:words)
        {
            string cur="";
            for(char c:s)
            {
                cur+=code[c-'a'];
            }
            out.insert(cur);
        }
        return out.size();
    }
};