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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* temp=new ListNode();
        temp->next=head;
        ListNode* p1=temp;
        ListNode* p2=temp;
        while (n>0)
        {
            p1=p1->next;
            n--;
        }
        while (p1!=nullptr && p1->next!=nullptr)
        {
            p1=p1->next;
            p2=p2->next;
        }
        p2->next=p2->next->next;
        return temp->next;
    }
};