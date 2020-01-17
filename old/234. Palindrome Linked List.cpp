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
    bool isPalindrome(ListNode* head) {
        if(!head || !head->next)
            return true;
        
        ListNode* slow = head;
        ListNode* fast = head;
        while(fast->next && fast->next->next)
        {
            slow = slow->next;
            fast = fast->next->next;
        }
        fast = slow->next;
        slow->next = nullptr;
        
        ListNode* cur = fast->next;
        fast->next = nullptr;
        while(cur)
        {
            ListNode* nex = cur->next;
            cur->next = fast;
            fast = cur;
            cur = nex;
        }
        while(head && fast)
        {
            if(head->val != fast->val)
                return false;
            head = head->next;
            fast = fast->next;
        }
        return true;
    }
};
