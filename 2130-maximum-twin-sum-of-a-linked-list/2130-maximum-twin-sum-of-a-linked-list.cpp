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
    int pairSum(ListNode* head) {
        int out=0;
        ListNode* p1=head;
        ListNode* p2=head;
        ListNode* pre=nullptr;
        ListNode* nex;
        while(p1 && p1->next && p1->next->next){
            p1=p1->next->next;
            nex=p2->next;
            p2->next=pre;
            pre=p2;
            p2=nex;
        }
        p1=p2->next;
        p2->next=pre;
        while(p1){
            out=max(out,p1->val+p2->val);
            p1=p1->next;
            p2=p2->next;
        }
        return out;
        
    }
};