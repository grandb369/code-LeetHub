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
    vector<double> averageOfLevels(TreeNode* root) {
        vector<double>out;
        vector<TreeNode*>stack{root};
        while(stack.size()>0)
        {
            vector<TreeNode*>temp;
            double val=0;
            double c=0;
            for(auto root:stack)
            {
                val+=root->val;
                c++;
                if(root->left)temp.push_back(root->left);
                if(root->right)temp.push_back(root->right);
            }
            stack=temp;
            if(c!=0)
            {
                out.push_back(val/c);
            }
            
        }
        return out;
    }
};