/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
 var addTwoNumbers = function(l1, l2) {
    let newNode = new ListNode();
    let head = newNode;
    let carry = 0;
    while(l1 || l2){
        let sum = (l1 ? l1.val : 0) + (l2 ? l2.val : 0) + carry;
        carry = 0;
        if(sum > 9){
            sum -=10;
            carry = 1;
        }
        head.val = sum;
        
        if(carry > 0){
            head.next = new ListNode(carry);
        }
        
        if(l1){
            l1 = l1.next;
        }
        if(l2){
            l2 = l2.next;
        }
        if(l1 || l2)
        {
            head.next = new ListNode();
            head = head.next;  
        }
        
    }    
    return newNode;
};