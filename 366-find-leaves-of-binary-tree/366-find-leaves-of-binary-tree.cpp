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
    int dfs(TreeNode* root, map<int,vector<int>>&temp)
    {
        if(root==nullptr)return 0;
        int left=dfs(root->left,temp);
        int right=dfs(root->right,temp);
        int depth=max(left,right);
        temp[depth].push_back(root->val);
        return depth+1;
    }
    vector<vector<int>> findLeaves(TreeNode* root) {
        map<int,vector<int>>temp;
        vector<vector<int>>out;
        dfs(root,temp);
        for(auto it=temp.begin();it!=temp.end();it++)
        {
            out.push_back(it->second);
        }
        return out;
    }
};