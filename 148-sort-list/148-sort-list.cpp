/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* merge(ListNode* head){
        if(!head->next)return head;
        if(!head->next->next)
        {
            ListNode* out=head;
            if(head->val>head->next->val)
            {
                out=head->next;
                head->next=nullptr;
                out->next=head;
            }
            return out;
        }
        ListNode* p1=head;
        ListNode* p2=head;
        while (p1 && p1->next)
        {
            p1=p1->next->next;
            p2=p2->next;
        }
        p1=p2->next;
        p2->next=nullptr;
        ListNode* left=merge(head);
        ListNode* right=merge(p1);
        ListNode* out=new ListNode();
        ListNode* root=out;
        while(left && right)
        {
            if(left->val<=right->val)
            {
                root->next=left;
                left=left->next;
            }
            else
            {
                root->next=right;
                right=right->next;
            }
            root=root->next;
        }
        root->next=nullptr;
        if(left)
        {
            root->next=left;
        }
        if(right)
        {
            root->next=right;
        }
        return out->next;
    }
    ListNode* sortList(ListNode* head) {
        if(!head)return head;
        return merge(head);
    }
};