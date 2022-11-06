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

 function deleteDuplicates(head: ListNode | null): ListNode | null {

    const t = new ListNode()
    t.next = head;


    let prev = t;
    let node = head;
    let dup = null;
    while(node && node.next){
        
        if(node.val === dup || node.next.val == node.val){
              dup = node.val;
              prev.next = node.next;
        }else{
            prev = prev.next;
        }
        node = node.next;

    }
    if(node && node.val == dup ){
         prev.next = null;
    }
    return t.next;
}