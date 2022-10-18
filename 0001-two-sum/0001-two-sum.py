class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {} #dictionary to hold value and index pair
        
        for i in range(len(nums)): ##iterates through nums
            complement = target - nums[i] #complement of i
            
            if complement in visited: #checks if complement of i exists in dictionary of previously visited values
                return [visited[complement], i] #if it is, return the index of the complement and current index
            else:
                visited[nums[i]] = i #if not add current index to i
            
            
        