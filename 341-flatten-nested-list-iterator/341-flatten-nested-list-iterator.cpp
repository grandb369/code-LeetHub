/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */

class NestedIterator {
public:
    vector<int>data;
    int i;
    int n;
    NestedIterator(vector<NestedInteger> &nums) {
        get(nums);
        i=0;
        n=data.size();
    }
    
    void get(vector<NestedInteger> &nums)
    {
        for(auto cur:nums)
        {
            if(cur.isInteger())
            {
                data.push_back(cur.getInteger());
            }
            else get(cur.getList());
        }
    }
    
    int next() {
        return data[i++];
    }
    
    bool hasNext() {
        return i<n;
    }
};

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i(nestedList);
 * while (i.hasNext()) cout << i.next();
 */