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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>>out;
        if(!root)return out;
        vector<TreeNode*>stack{root};
        while(stack.size()>0)
        {
            vector<int>temp;
            vector<TreeNode*>nex;
            for(auto root:stack)
            {
                temp.push_back(root->val);
                if(root->left)
                {
                    nex.push_back(root->left);
                }
                if(root->right)
                {
                    nex.push_back(root->right);
                }
            }
            stack=nex;
            out.push_back(temp);
        }
        return out;
    }
};