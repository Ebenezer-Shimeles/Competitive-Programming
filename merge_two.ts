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

 function mergeTwoLists(list1: ListNode | null, list2: ListNode | null): ListNode | null {
    if(list1 == null) return list2 
    if(list2 == null) return list1 

    const smaller = list1.val > list2.val ? list2.val : list1.val;
    list1.val > list2.val ? list2 = list2.next : list1 = list1.next;
    let n = new ListNode(smaller, null);
    const top = n;

    while(list1 != null && list2 != null){
        if(list1.val < list2.val){
            console.log("#1 ", list1.val, ' < ', list2.val)
           n.next = new ListNode(list1.val, null)
         
             list1 = list1.next;
        }else{
            console.log("#2 ", list2.val, ' < ', list1.val)
              n.next = new ListNode(list2.val, null)
            list2 = list2.next;  
        }
        n = n.next;
       
       
    }
    if(list1 != null){
        n.next = list1;
    }
    if(list2 != null){
        n.next = list2;
    }
    return top;   
};