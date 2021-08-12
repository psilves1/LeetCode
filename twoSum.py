class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = 0
        while(n < len(nums)):
            
            i = n+1
            while(i < len(nums)):
                
                if(nums[i] + nums[n] == target):
                    return [n,i]
                
                i+=1
            
            n+=1
        return [-1,-1]
