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
    TreeNode* dfs(TreeNode* root)
    {
        if(!root)
        {
            return root;
        }
        root->left=dfs(root->left);
        root->right=dfs(root->right);
        if (root->val==0 && !root->left && !root->right)
        {
            return nullptr;
        }
        return root;
    }
    TreeNode* pruneTree(TreeNode* root) {
        return dfs(root);
    }
};