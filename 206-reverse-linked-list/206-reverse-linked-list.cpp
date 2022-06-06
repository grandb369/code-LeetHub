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
    ListNode* reverseList(ListNode* head) {
        if (!head || !head->next)return head;
        ListNode* pre=nullptr;
        ListNode* cur=head;
        ListNode* nex=head->next;
        while(nex)
        {
            ListNode* nexnex=nex->next;
            nex->next=cur;
            cur->next=pre;
            pre=cur;
            cur=nex;
            nex=nexnex;
        }
        return cur;
    }
};