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
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode* temp = head;
        int ct = 0;
        while(ct<k){
            if(temp == NULL){
                return head;
            }
            temp = temp->next;
            ct++;
        }
        ListNode* newNode = reverseKGroup(temp,k);

        temp = head;
        ct = 0;

        while(ct<k){
            ListNode* next = temp->next;
            temp->next = newNode;

            newNode = temp;
            temp = next;

            ct++;
        }
    return newNode;
    }
};