class Solution:
    def reverse(self, x: int) -> int:
        
        isNeg = False
        
        if(x < 0):
            x *= -1
            isNeg = True
        
        x = str(x)
        
        """ 
        #Original solution
        
        arr = [""] * len(x)
        
        for i in range(int(len(x)/2)):
            temp = x[i]
            arr[i] = x[len(x) - i - 1]
            arr[len(x) - i - 1] = temp
            
        if(len(x)%2==1):
            arr[int(len(x)/2)] = x[int(len(x)/2)]
            
        x = ""
        
        for i in range(len(arr)):
            x = x + arr[i]
        
        """
        #Second Solution. Very memory efficient
        x = x[::-1]
        
        x = int(x)
        
        if(x > 2147483647 or x < -2147483648):
            return 0
        
        if(isNeg):
            return x * -1
                    
        return x
