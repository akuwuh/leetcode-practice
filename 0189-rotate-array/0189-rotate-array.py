class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if len(nums) != 2:
            nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]     
        elif k%2 == 1:
            nums[:] = nums[1:] + nums[:1]
        