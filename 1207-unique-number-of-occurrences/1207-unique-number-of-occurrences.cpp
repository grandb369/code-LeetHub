class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        unordered_map<int,int> k;
        unordered_set<int> temp;
        for (int i: arr)
        {
            k[i]++;
        }
        for (auto i:k)
        {
            if(temp.find(i.second)!=temp.end())
            {
                return false;
            }
            temp.insert(i.second);
        }
        return true;
    }
};