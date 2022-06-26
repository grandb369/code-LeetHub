class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char,int>k;
        k['I']=1;
        k['V']=5;
        k['X']=10;
        k['L']=50;
        k['C']=100;
        k['D']=500;
        k['M']=1000;
        int out=0;
        char pre='\0';
        for (char i:s)
        {
            out+=k[i];
            if(pre=='I' && (i=='V' || i=='X'))out-=2;
            if(pre=='X' && (i=='L' || i=='C'))out-=20;
            if(pre=='C' && (i=='D' || i=='M'))out-=200;
            pre=i;
        }
        return out;
    }
};