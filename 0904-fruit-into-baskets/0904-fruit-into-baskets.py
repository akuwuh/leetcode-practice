from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        seen = defaultdict(int)
        maxlen = 0

        for i, v in enumerate(fruits):
            seen[v] += 1

            while len(seen) > 2: 
                seen[fruits[l]] -= 1
                if seen[fruits[l]] == 0:
                    del seen[fruits[l]]
                l += 1
            curr = i - l + 1
            maxlen = max(curr,maxlen)

        return maxlen

        #[3,3,3,1,2,1,1,2,3,3,4]