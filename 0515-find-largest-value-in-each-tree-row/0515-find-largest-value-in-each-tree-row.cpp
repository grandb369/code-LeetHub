/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> largestValues(TreeNode* root) {
        vector<int> out;
        if(!root)return out;
        vector<TreeNode*>stack{root};
        while(stack.size()!=0){
            vector<TreeNode*>nex;
            int val=stack[0]->val;
            for(auto cur:stack){
                val=max(val,cur->val);
                if(cur->left)nex.push_back(cur->left);
                if(cur->right)nex.push_back(cur->right);
            }
            stack=nex;
            out.push_back(val);
        }
        return out;
    }
};