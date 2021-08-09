/* Add Two Numbers */
/* Solution by Arjun Mehta*/

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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        
        /* Declare required variables. */
        int carry = 0;
        int value = 0;
        ListNode *answer = new ListNode(0);
        ListNode *answer_head  = answer;
        
        /* Loop till both linked lists have ended. */
        while(l1!=nullptr || l2!=nullptr){
            
            /* Set value based on l1 and l2 val. */
            if(l1 == nullptr) value = l2->val;
            else if(l2 == nullptr) value =  l1->val;
            else value = l1->val + l2->val;
            
            /* Set next node of answer list and set carry. */
            if((value+carry)>9){
                answer->next = new ListNode((value-10) + carry);
                carry = 1;
            } else{
                answer->next = new ListNode(value+carry);
                carry = 0;
            }
            
            /* Advance current nodes of l1, l2 and answer list to next node. */
            if(l1!=nullptr) l1=l1->next;
            if(l2!=nullptr) l2=l2->next;
            answer = answer->next;
        }
        
        /* If carry is 1 after while loop, set the value of next node of answer list as 1*/
        if(carry == 1) answer->next = new ListNode(carry);
        
        /* Return the root of answer list. */
        return answer_head->next;
    }
};
