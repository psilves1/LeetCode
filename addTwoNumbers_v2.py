# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Originally I was going to use loops, but after some consideration
#I think that using recursion might be the better solution


class Solution:    
    
    #list[0] is retVal.val and list[1] is overflow
    def adder(self, a = 0, b = 0, c = 0) -> list:
        temp = a + b + c
        overflow = 0
        
        if(temp >= 10):
            temp -= 10
            overflow = 1
        return [temp,overflow]            
        
    
    #'of' stands for 'overflow'
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], of = 0, firstNode = True) -> Optional[ListNode]:
        
        retVal = ListNode()
        
        if(l1 != None and l2 != None):
            
            arr = self.adder(l1.val, l2.val, of)    
            
            retVal.val = arr[0]
                        
            retVal.next = self.addTwoNumbers(l1.next, l2.next, arr[1], False) #recursion
            
        elif(l1 != None): #l2 == None
            
            arr = self.adder(l1.val, of)    
            
            retVal.val = arr[0]
            
            retVal.next = self.addTwoNumbers(l1.next, None, arr[1], False) #recursion
            
        elif(l2 != None): #l1 = None
            arr = self.adder(l2.val, of)    
            
            retVal.val = arr[0]
            
            retVal.next = self.addTwoNumbers(l2.next, None, arr[1], False) #recursion
            
        else:
            retVal.val = of
            
                    
        if(retVal.next == None and retVal.val == 0 and not firstNode):
            retVal = None
            
        
        return retVal
