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
    ListNode* deleteDuplicates(ListNode* head) {
        if(!head || !head->next)return head;
        ListNode* pre=head;
        ListNode* cur=head->next;
        while(cur)
        {
            if(cur->val==pre->val)cur=cur->next;
            else
            {
                pre->next=cur;
                pre=cur;
                cur=cur->next;
            }
        }
        pre->next=cur;
        return head;
    }
};