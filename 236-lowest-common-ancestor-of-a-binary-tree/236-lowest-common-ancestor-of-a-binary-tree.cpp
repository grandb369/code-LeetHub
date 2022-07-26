/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(root!=nullptr)
        {
            TreeNode* left=lowestCommonAncestor(root->left,p,q);
            TreeNode* right=lowestCommonAncestor(root->right,p,q);
            if(left==nullptr && right==nullptr)return root==p || root==q?root:nullptr;
            else if(left!=nullptr && right!=nullptr)return root;
            else if(left!=nullptr)return root==p || root==q?root:left;
            else return root==p || root==q?root:right;
        }
        return nullptr;
    }
};