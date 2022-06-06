/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode* temp=new ListNode();
        temp->next=head;
        ListNode* p1=temp;
        ListNode* p2=temp;
        while(p1 && p1->next)
        {
            p1=p1->next->next;
            p2=p2->next;
            if(p1==p2)return true;
        }
        return false;
    }
};