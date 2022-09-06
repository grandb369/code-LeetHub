/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    vector<vector<int>> levelOrder(Node* root) {
        vector<vector<int>>out;
        if(root==nullptr)return out;
        vector<Node*> stack{root};
        while(stack.size()>0)
        {
            vector<int>ans;
            vector<Node*>temp;
            for(auto root:stack)
            {
                ans.push_back(root->val);
                for(auto nex:root->children)
                {
                    temp.push_back(nex);
                }
            }
            stack=temp;
            out.push_back(ans);
        }
        return out;
    }
};