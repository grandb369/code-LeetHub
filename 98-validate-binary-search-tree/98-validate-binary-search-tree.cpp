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
    vector<int> dfs(TreeNode* root, bool &ans)
    {
        int mi=root->val;
        int ma=root->val;
        if(root->left)
        {
            vector<int>l=dfs(root->left,ans);
            if(l[1]>=mi)ans=false;
            mi=min(mi,l[0]);
        }
        if(root->right && ans)
        {
            vector<int>r=dfs(root->right,ans);
            if(r[0]<=ma)ans=false;
            ma=max(ma,r[1]);
        }
        return vector<int>{mi,ma};
        
    }
    bool isValidBST(TreeNode* root) {
        bool out=true;
        dfs(root,out);
        return out;
    }
};