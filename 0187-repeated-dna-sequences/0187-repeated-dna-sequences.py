class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n < 11: 
            return []
        # if longer than 10
        seen = defaultdict()
        ans = set()
        for i in range(10,n + 1):
            new = s[i-10:i]

            if new in seen:
                ans.add(new)
                continue
            
            seen[new] = 0

        return ans


