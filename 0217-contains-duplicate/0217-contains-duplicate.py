from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = dict(Counter(nums))
        
        for key in seen:
            if seen[key] > 1: 
                return True
        return False