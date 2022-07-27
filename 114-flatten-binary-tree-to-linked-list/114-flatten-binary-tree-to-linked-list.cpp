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
    void flatten(TreeNode* root) {
        vector<TreeNode*>stack{root};
        TreeNode* pre=nullptr;
        while (stack.size()>0)
        {
            root=stack.back();
            stack.pop_back();
            while (root)
            {
                stack.push_back(root->right);
                if(pre)
                {
                    pre->right=root;
                }
                pre=root;
                root=root->left;
                pre->left=nullptr;
            }
        }
    }
};