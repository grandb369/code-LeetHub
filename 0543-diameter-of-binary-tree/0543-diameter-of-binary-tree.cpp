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
    vector<int> dfs(TreeNode* root){
        vector<int>out={0,0};
        if (!root)
        {
            return out;
        }
        out=dfs(root->left);
        vector<int>temp=dfs(root->right);
        //cout<<root->val<<endl;
        //cout<<out[0]<<'\t'<<out[1]<<endl;
        //cout<<temp[0]<<'\t'<<temp[1]<<endl;
        out[1]=max(out[1],out[0]+temp[0]+1);
        out[1]=max(out[1],temp[1]);
        out[0]=max(out[0],temp[0])+1;
        //cout<<out[0]<<'\t'<<out[1]<<endl;
        return out;
    }
    int diameterOfBinaryTree(TreeNode* root) {
        vector<int>out=dfs(root);
        return out[1]-1;
    }
};