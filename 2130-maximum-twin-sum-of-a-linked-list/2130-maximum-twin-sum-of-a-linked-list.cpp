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
        vector<int>temp;
        int c=0;
        while(head){
            temp.push_back(head->val);
            head=head->next;
            c++;
        }
        int out=0;
        for(int i=0;i<c/2;i++){
            out=max(out,temp[i]+temp[c-1-i]);
        }
        return out;
    }
};