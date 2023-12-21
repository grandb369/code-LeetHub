class Solution {
public:
    int maxWidthOfVerticalArea(vector<vector<int>>& points) {
        sort(points.begin(),points.end());
        int out=0;
        int pre=points[0][0];
        for(vector<int> v:points){
            int cur=v[0];
            out=max(out,cur-pre);
            pre=cur;
        }
        return out;
    }
};