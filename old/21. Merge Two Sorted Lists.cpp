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
//lower speed version
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if(l2 == NULL)
            return l1;
        if(l1 == NULL)
            return l2;
        ListNode node = ListNode(INT_MIN);
        ListNode *head = &node;
        while(l1!=NULL && l2!=NULL) {
            if(l1->val > l2->val ) {
                head->next = l2;
                l2 = l2->next;
            } 
            else {
                head->next = l1;
                l1 = l1->next;
            }
            head = head->next;
        }
        if(l1!=NULL)
            head->next = l1;
        else
            head->next = l2;
        return node.next;
    }
//quick version using recursion
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {   
        if(l1 == NULL)
            return l2;
        if(l2 == NULL)
            return l1;
        if(l1->val < l2->val)
        {
            l1->next = mergeTwoLists(l1->next,l2);
            return l1;
        }
        else
        {
            l2->next = mergeTwoLists(l1,l2->next);
            return l2;    
        } 
    }
};