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
    void dfs(vector<int> &temp, vector<vector<int>>& out, TreeNode* root, int val, int target)
    {
        if(!root->left && !root->right)
        {
            val+=root->val;
            temp.push_back(root->val);
            if(val==target)
            {
                out.push_back(temp);
            }
            temp.pop_back();
        }
        else
        {
            temp.push_back(root->val);
            val+=root->val;
            if(root->left)dfs(temp,out,root->left,val,target);
            if(root->right)dfs(temp,out,root->right,val,target);
            temp.pop_back();
        }
    }
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        vector<vector<int>>out;
        vector<int>temp;
        if(root)dfs(temp,out,root,0,targetSum);
        return out;
    }
};