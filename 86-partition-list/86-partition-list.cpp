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
    ListNode* partition(ListNode* head, int x) {
        ListNode* s=new ListNode();
        ListNode* l=new ListNode();
        ListNode* s_head=s;
        ListNode* l_head=l;
        while(head)
        {
            if (head->val<x)
            {
                s->next=head;
                s=s->next;
            }
            else
            {
                l->next=head;
                l=l->next;
            }
            head=head->next;
        }
        l->next=nullptr;
        s->next=l_head->next;
        return s_head->next;
    }
};