class Solution {
public:
    int findSpecialInteger(vector<int>& arr) {
        int out=arr[0];
        map<int,int> temp;
        int n=arr.size();
        for(int i:arr){
            temp[i]++;
            if(temp[i]>n/4)out=i;
        }
        return out;
    }
};