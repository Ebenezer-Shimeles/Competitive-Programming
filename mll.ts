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

 function middleNode(head: ListNode | null): ListNode | null {
    let temp = head;
     let listLen = 0;
     while(head.next !=null)
    {
        head = head.next;
        listLen++;
    }
    for(let i=0;i<listLen/2;i++){
        temp = temp.next;
    }
    return temp

};