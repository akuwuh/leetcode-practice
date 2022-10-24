class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = {}
        
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen[nums[i]] = 1 #adding value at index to seen and keeping track of how many has been seen
            else:
                seen[nums[i]] +=1
            
        for i in seen:
            if seen[i] != 2:
                return i
            
