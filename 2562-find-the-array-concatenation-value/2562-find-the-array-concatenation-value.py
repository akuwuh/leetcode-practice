class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        ans = 0
        while nums:
            
            if len(nums) == 1:
                ans += nums[0]
                break
            else:
                ans += int(str(nums[0]) + str(nums[-1]))
                nums.pop(0)
                nums.pop(-1)
        return ans
            