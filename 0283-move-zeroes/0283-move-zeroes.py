class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        nums[:] = [i for i in nums if i != 0] +  [0]*nums.count(0)