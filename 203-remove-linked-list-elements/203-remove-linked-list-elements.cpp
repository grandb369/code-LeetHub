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
    ListNode* removeElements(ListNode* head, int val) {
        ListNode* temp=new ListNode();
        temp->next=head;
        ListNode* pre=temp;
        ListNode* cur=head;
        while(cur)
        {
            if(cur->val==val)
            {
                cur=cur->next;
                pre->next=cur;
            }
            else
            {
                cur=cur->next;
                pre=pre->next;
            }
        }
        return temp->next;
    }
};