class Solution {
public:
    long minMoves2(vector<int>& nums) {
        long l=(int)pow(10,9);
        long r=(int)-pow(10,9);
        long out =(long)pow(2,31);
        for(long i:nums)
        {
            l=min(l,i-1);
            r=max(r,i+1);
        }
        while (l<r)
        {
            long mid=(int)(l+r)/2;
            long v1=0;
            long v2=0;
            for(long i:nums)
            {
                v1+=abs(i-mid);
                v2+=abs(i-mid-1);
            }
            //cout<<l<<','<<r<<"        "<<mid<<"      ;"<<v1<<','<<v2<<"       "<<out<<endl;
            if(v2>v1)
            {
                out=min(out,v1);
                r=mid-1;
            }
            else 
            {
                out=min(out,v2);
                l=mid+1;
            }
            
        }
        return out;
        
    }
};