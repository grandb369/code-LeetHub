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
    TreeNode* build(vector<int>& preorder, int l, int r, vector<int>& inorder, int i, int j){
        if(l<=r && i<=j)
        {
            int cur=preorder[l];
            TreeNode* root=new TreeNode(cur);
            int index=i;
            for(int x=i;x<=j;x++)
            {
                if(inorder[x]==cur)
                {
                    index=x-1;
                    break;
                }
            }
            root->left=build(preorder,l+1,l+1+index-i,inorder,i,index);
            root->right=build(preorder,l+index+2-i,r,inorder,index+2,j);
            return root;
        }
        return nullptr;
    }
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        return build(preorder,0,preorder.size()-1,inorder,0,inorder.size()-1);
    }
};