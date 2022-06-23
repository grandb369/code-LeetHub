class Solution {
public:
    string greatestLetter(string s) {
        string out="";
        char val='\0';
        set<char> temp;
        for(char i:s)
        {
            if(isupper(i) && temp.find(tolower(i))!=temp.end())
            {
                if(!val)val=i;
                else val=max(val,i);
            }
            else if(islower(i) && temp.find(toupper(i))!=temp.end())
            {
                i=toupper(i);
                if(!val)val=i;
                else val=max(val,i);
            }
            temp.insert(i);
        }
        if(val)out+=val;
        return out;
    }
};