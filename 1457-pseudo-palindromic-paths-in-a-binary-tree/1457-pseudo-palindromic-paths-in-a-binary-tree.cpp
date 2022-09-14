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
    int dfs(TreeNode* root, vector<int>& temp){
        if(!root->left && !root->right)
        {
            temp[root->val]++;
            int c=0;
            for(int i:temp)
            {
                if(i%2==1)c++;
            }
            temp[root->val]--;
            return c<=1?1:0;
        }
        int out=0;
        temp[root->val]++;
        if(root->left)
        {
            
            out+=dfs(root->left,temp);
            
        }
        if(root->right)
        {
            out+=dfs(root->right,temp);
        }
        temp[root->val]--;
        return out;
    }
    int pseudoPalindromicPaths (TreeNode* root) {
        vector<int>temp(10,0);
        return dfs(root,temp);
    }
};