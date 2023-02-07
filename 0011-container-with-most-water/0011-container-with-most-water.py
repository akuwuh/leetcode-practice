from collections import defaultdict

class Solution:
    def maxArea(self, height: List[int]) -> int:

        seen = defaultdict() #val, area

        l = 0 
        r = len(height) - 1
        ans = (r-l) * min(height[r], height[l])

        while l < r:
            if(height[l] < height[r]):
                l += 1
            else:
                r -= 1
            ans = max(ans, (r-l) * min(height[r], height[l]))

            
       
        return ans

        
            
            
        # 2 3 10 5 7 8 9                
        # 0 1 2  3 4 5 6 7 8 





            