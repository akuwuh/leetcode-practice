class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        ans = l = 0
        curr = 1

        for i,val in enumerate(nums):
            curr *= val
            ans+=1
            while curr >= k:
                curr //= nums[l]
                l+=1
            ans += i - l
        
        return ans


        
            