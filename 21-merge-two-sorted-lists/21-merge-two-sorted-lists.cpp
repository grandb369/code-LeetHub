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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if(!l1)return l2;
        if(!l2)return l1;
        ListNode* out=nullptr;
        ListNode* cur=nullptr;
        while(l1 && l2)
        {
            if(l1->val<l2->val)
            {
                if(!out)
                {
                    out=l1;
                    cur=l1;
                }
                else
                {
                    cur->next=l1;
                    cur=cur->next;
                }
                l1=l1->next;
            }
            else
            {
                if(!out)
                {
                    out=l2;
                    cur=l2;
                }
                else
                {
                    cur->next=l2;
                    cur=cur->next;
                }
                l2=l2->next; 
            }
        }
        if(l1)cur->next=l1;
        if(l2)cur->next=l2;
        return out;
    }
};