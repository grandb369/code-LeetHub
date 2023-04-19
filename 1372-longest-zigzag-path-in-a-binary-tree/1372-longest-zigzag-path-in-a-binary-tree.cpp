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
    int out=0;
    int longestZigZag(TreeNode* root, int pre=-1, int val =0) {
        if (!root)return val;
        out=max(out,val);
        if(root->left) out=max(out, longestZigZag(root->left, 0, pre==1?val+1:1));
        if(root->right) out=max(out,longestZigZag(root->right,1,pre==0?val+1:1));
        return out;
    }
};