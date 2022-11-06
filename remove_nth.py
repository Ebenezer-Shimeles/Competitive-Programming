# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast: ListNode = head
        slow: ListNode = head
        top: ListNode = head
        prev : ListNode = head
    
        t = 0
        print(fast)
        while fast != None:
           
            fast = fast.next
            t += 1
        print(f'{t-n}')
        u = 0
        while slow != None:
            if u == t - n :
                print(f'deleting {t-n}')
                if slow.next:
                     slow.val = slow.next.val
                     slow.next = slow.next.next
                else:
                    if t == 1:
                        return None
                    print('here')
                    
                    prev.next= None
                
                     #slow.val
                     #slow.next= None
                    # del slow.val

            prev = slow  
            slow = slow.next
            
            u += 1
           
        print(f'Total: {t}')
        return top
