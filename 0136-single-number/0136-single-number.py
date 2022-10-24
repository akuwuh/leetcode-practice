from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        seen = dict(Counter(nums))
            
        for i in seen:
            if seen[i] != 2:
                return i
            
