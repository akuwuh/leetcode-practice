class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        largest = 0
        seen = set()

        p1 = 0


        for p2 in range(len(s)):
            while s[p2] in seen: #if duplicate encountered
                seen.remove(s[p1])
                p1+=1
            seen.add(s[p2])
            largest = max(len(seen), largest)

        
        return largest


            
        
        
