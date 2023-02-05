import itertools
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        if nums[0] == nums[-1] == 0: # if they are all zeroes
            return [[0,0,0]]   

        ans = []   


        if len(nums) == 3 and nums[0] + nums[1] + nums[2] == 0:
            return [nums]

        for i in range(len(nums) - 3):
            seen = {}
            target = 0 - nums[i]

            temp = nums[i+1:]
            for k, j in enumerate(temp):
                r = target - j
                if r in seen: 
                    ans.append([nums[i], j, r])
                seen[j] = k

          

        return list(set([tuple(sorted(index)) for index in ans]))



        # only possible if in sorter array there is a postiive and negative number at the end are all 0's 
        # -1 0 1 2 -1 -4
        # -4 -1 -1 0 1 2
        #  ^ needed = 4 
        # -> -1 -1 0 1 2




