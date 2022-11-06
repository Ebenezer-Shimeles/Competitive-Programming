/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

 function reverseList(head: ListNode | null): ListNode | null {
    let prev = null;
    let tmp = null;
    while(head!=null){
        
           
        
        tmp = prev
       
        prev = new ListNode(head?.val, tmp)
         head = head.next;
      
       //  tmp = prev;
       //  prev = head;
       //  prev.next = tmp;
    }
    return prev;
};