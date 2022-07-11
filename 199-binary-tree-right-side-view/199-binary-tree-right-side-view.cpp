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
    vector<int> rightSideView(TreeNode* root) {
        vector<int> out;
        vector<TreeNode*> stack;
        if (root!=nullptr)
        {
            stack.push_back(root);
        }
        while(stack.size()>0)
        {
            vector<TreeNode*>temp;
            int last=101;
            for(auto root:stack)
            {
                last=root->val;
                if(root->left)
                {
                    temp.push_back(root->left);
                }
                if(root->right)
                {
                    temp.push_back(root->right);
                }
            }
            stack=temp;
            if(last!=101)
            {
                out.push_back(last);
            }
        }
        return out;
    }
};