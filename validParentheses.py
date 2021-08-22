class Solution:
    
    @staticmethod
    def add_char(stack: list, c:str) -> None:
        stack.insert(0,c)
    
    @staticmethod
    def remove_char(stack: list, c:str) -> bool:
        if(len(stack) == 0):       #make sure stack isn't empty
            return False
        
        char = stack.pop(0)
        
        if(char == "(" and c == ")"):
            return True
        if(char == "{" and c == "}"):
            return True
        if(char == "[" and c == "]"):
            return True
        
        return False
        
    
    
    def isValid(self, s: str) -> bool:
        
        if(len(s)%2==1):
            return False
        
        stack = []  
        
        success = True
        
        for c in s:
            if(c == "(" or c == "[" or c == "{"):
                Solution.add_char(stack,c)
            elif(c == ")" or c == "]" or c == "}"):
                if(not Solution.remove_char(stack,c)):
                    return False
        
        return len(stack) == 0
        
        
        
