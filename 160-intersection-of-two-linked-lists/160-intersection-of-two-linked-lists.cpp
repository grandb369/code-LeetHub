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
    ListNode *getIntersectionNode(ListNode *h1, ListNode *h2) {
        ListNode* p1=h1;
        ListNode* p2=h2;
        if(p1==p2)return p1;
        int c1=1;
        int c2=1;
        
        while(p1!=nullptr && p2!=nullptr)
        {
            p1=p1->next;
            p2=p2->next;
            
            if(p1==nullptr && c1>0)
            {
                p1=h2;
                c1--;
            }
            if (p2==nullptr && c2>0)
            {
                p2=h1;
                c2--;
            }
            if (p1==p2)return p1;
            
        }
        return p1;
    }
};