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
    int kthSmallest(TreeNode* root, int k) {
        vector<TreeNode*> stack{root};
        while(stack.size())
        {
            root=stack.back();
            stack.pop_back();
            while(root)
            {
                stack.push_back(root->right);
                stack.push_back(root);
                root=root->left;
            }
            
            root=stack.back();
            stack.pop_back();
            if (root)
            {
                k-=1;
                if(k==0)return root->val;
            }
        }
        return 0;
    }
};