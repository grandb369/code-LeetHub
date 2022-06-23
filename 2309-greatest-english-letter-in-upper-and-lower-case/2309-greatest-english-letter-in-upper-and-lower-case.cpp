class Solution {
public:
    string greatestLetter(string s) {
        char out='\0';
        set<char> temp;
        for(char i:s)
        {
            if(isupper(i) && temp.find(tolower(i))!=temp.end())
            {
                if(!out)out=i;
                else out=max(out,i);
            }
            else if(islower(i) && temp.find(toupper(i))!=temp.end())
            {
                i=toupper(i);
                if(!out)out=i;
                else out=max(out,i);
            }
            temp.insert(i);
        }
        if(out=='\0')return "";
        string ans="";
        ans+=out;
        return ans;
    }
};