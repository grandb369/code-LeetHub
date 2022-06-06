/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/

class Solution {
public:
    Node* connect(Node* root) {
        if(!root)return root;
        Node* out=root;
        vector<Node*>stack{root};
        while (stack.size()>0)
        {
            vector<Node*>temp;
            Node* pre=nullptr;
            for(Node* cur:stack)
            {
                if(pre)pre->next=cur;
                if(cur->left)temp.push_back(cur->left);
                if(cur->right)temp.push_back(cur->right);
                pre=cur;
            }
            stack=temp;
        }
        return out;
    }
};