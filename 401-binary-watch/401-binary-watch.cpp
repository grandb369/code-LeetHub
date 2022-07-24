class Solution {
public:
    void back(int n, vector<string>&out, int h, int m, int lh, int lm, set<string>&seen)
    {
        if(n==0)
        {
            if(h<12 && m<60)
            {
                string hour=to_string(h);
                string mins=to_string(m);
                if (mins.size()==1)
                {
                    mins="0"+mins;
                }
                string s=hour+":"+mins;
                if (seen.find(s)==seen.end())
                {
                    out.push_back(s);
                    seen.insert(s);
                }
                
            }
            
            
        }
        else
        {
            
            for(int i:{1,2,4,8,16,32})
            {
                if(i<=lm)continue;
                back(n-1,out,h,m+i,lh,i,seen);
            }
            for(int i:{1,2,4,8})
            {
                if(i<=lh)continue;
                back(n-1,out,h+i,m,i,lm,seen);
            }
        }
    }
    vector<string> readBinaryWatch(int n) {
        vector<string>out;
        set<string>seen;
        if(n>8)return out;
        back(n,out,0,0,0,0,seen);
        return out;
    }
};