# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Originally I was going to use loops, but after some consideration
#I think that using recursion might be the better solution


class Solution:    
    #'of' stands for 'overflow'
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], of = 0, firstNode = True) -> Optional[ListNode]:
        
        retVal = ListNode()
        
        if(l1 != None and l2 != None):
            temp = l1.val + l2.val + of
            overflow = 0
            
            if(temp >= 10):
                temp -= 10
                overflow = 1
                
            
            retVal.val = temp
                        
            retVal.next = self.addTwoNumbers(l1.next, l2.next, overflow, False) #recursion
            
        elif(l1 != None):
            temp = l1.val + of
            overflow = 0
            
            if(temp >= 10):
                temp -= 10
                overflow = 1
            
            retVal.val = temp
            
            retVal.next = self.addTwoNumbers(l1.next, None, overflow, False) #recursion
        elif(l2 != None):
            temp = l2.val + of
            overflow = 0
            
            if(temp >= 10):
                temp -= 10
                overflow = 1
            
            retVal.val = temp
            
            retVal.next = self.addTwoNumbers(l2.next, None, overflow, False) #recursion
        else:
            retVal.val = of
            
        
            
    #TODO Get rid of end Zero,also fix [0] + [0] edge case
            
        if(retVal.next == None and retVal.val == 0 and not firstNode):
            retVal = None
            
        
        return retVal
    
