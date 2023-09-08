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
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        if(left==right)return head;
        ListNode* out=new ListNode();
        ListNode* p1;
        out->next=head;
        p1=out;
        while(left>1)
        {
            left--;
            right--;
            p1=p1->next;
        }
        ListNode* cur=p1->next;
        ListNode* tail=cur;
        ListNode* nex=cur->next;
        ListNode* p2=nullptr;
        ListNode* pre=nullptr;
        while(right>1)
        {
            right--;
            p2=nex->next;
            nex->next=cur;
            cur->next=pre;
            pre=cur;
            cur=nex;
            nex=p2;
        }
        p1->next=cur;
        tail->next=p2;
        return out->next;
    }
};