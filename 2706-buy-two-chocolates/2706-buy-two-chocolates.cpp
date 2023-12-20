class Solution {
public:
    int buyChoco(vector<int>& prices, int money) {
        int v1,v2=-1;
        for(int v:prices){
            if(v1==-1)v1=v;
            else if(v2==-1){
                if(v<v1){
                    v2=v1;
                    v1=v;
                }
                else v2=v;
            }
            else{
                if(v1>=v){
                    v2=v1;
                    v1=v;
                }
                else if(v2>v)v2=v;
            }
        }
        cout<<v1<<','<<v2<<','<<money<<endl;
        cout<<money-v1-v2<<endl;
        cout<<(v1+v2<=money?money-v1-v2:money)<<endl;
        return v1+v2<=money?money-v1-v2:money;
    }
};