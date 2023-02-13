class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n < 11: 
            return []
        # if longer than 10
        seen = defaultdict()
        ans = []
        for i in range(10,n + 1):
            new = s[i-10:i]

            if new in seen and new not in ans:
                ans.append(new)
                continue
            
            seen[new] = 0

        return ans


