class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left = []
        right = []
        
        for i in range(len(nums)):
            
            if i == 0: 
                left.append(1)
            else:
                left.append(nums[i-1] * left[i-1])
        
        reverse = nums[::-1]
        
        
        for i in range(len(reverse)):
            
            if i == 0: 
                right.append(1)
            else:
                right.append(reverse[i-1] * right[i-1])
                
        right = right[::-1]
        answer = []
        
        for i in range(len(right)):
            answer.append(right[i] * left[i])
            
    
        return answer
            
            
        