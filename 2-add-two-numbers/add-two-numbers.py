# Definition for singly-linked list.

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        output = ListNode()
        curr = output
        carryover = False
        carryoverVal = 0

        while True:
            if l1 is None:
                l1 = ListNode()

            if l2 is None:
                l2 = ListNode()

            
           
            
                
            if carryover:
                carryoverVal = 1
            else:
                carryoverVal = 0
            


            curr.val = (l1.val +  l2.val + carryoverVal) % 10
            carryover =  (l1.val +  l2.val + carryoverVal) > 9

            if l1.next is not None or l2.next is not None or carryover:
                nextt = ListNode()
            else:
                nextt = None
            curr.next = nextt
        
            
            curr = nextt

            l1 = l1.next
            l2 = l2.next

            if nextt is None:

                break
           

        return output
            

