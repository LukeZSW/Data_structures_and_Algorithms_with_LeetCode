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
    ListNode* reverseList(ListNode* head) {
        if(head == nullptr) 
            return nullptr;
        ListNode* prevp = nullptr;
        ListNode* currp = head;
        ListNode* nextp = head->next;
        while (nextp != nullptr) {
            currp->next = prevp;
            prevp = currp;
            currp = nextp;
            nextp = nextp->next;
        }
        currp->next = prevp;
        return currp;
    }
};