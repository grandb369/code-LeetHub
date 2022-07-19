class Solution {
public:
    vector<int> assignTasks(vector<int>& servers, vector<int>& tasks) {
        //priority_queue<vector<long>, vector<vector<long>>,greater<vector<long>>>busy;
        //priority_queue<vector<long>, vector<vector<long>>,greater<vector<long>>>wait;
        priority_queue<array<long, 3>, vector<array<long, 3>>, greater<array<long, 3>>> wait, busy;
        vector<int>out;
        for(int i=0;i<servers.size();i++)
        {
            wait.push({servers[i],i,0});
        }
        for(int i=0;i<tasks.size();i++)
        {
            long index=i;
            long time=tasks[i];
            while(wait.size()==0 || busy.size()>0 && busy.top()[0]<=index)
            {
                auto temp=busy.top();
                busy.pop();
                wait.push({temp[1],temp[2],temp[0]});
            }
            auto nex=wait.top();
            wait.pop();
            out.push_back(nex[1]);
            busy.push({max(index,nex[2])+time, nex[0],nex[1]});
        }
        return out;
    }
};