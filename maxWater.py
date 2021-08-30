class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        back = len(height)-1
        front = 0
        maxArea = 0
        
        for n in range(len(height)):
            
            if(front == back):
                break
                
            if((back-front)*min(height[front],height[back]) > maxArea):
                maxArea = (back-front)*min(height[front],height[back])
                
            if(height[front] < height[back]):
                front+=1
            else:
                back-=1
            
        return maxArea
