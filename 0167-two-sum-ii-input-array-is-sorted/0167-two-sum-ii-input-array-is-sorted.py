class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        lo = 0
        hi = len(numbers) - 1
        
        while hi - lo != 1:
            if numbers[hi] + numbers[lo] == target:
                return [lo + 1, hi +1]
            
            if numbers[hi] + numbers[lo] > target: 
                hi -= 1
            else: 
                lo += 1
            
        
        return [lo + 1, hi +1]