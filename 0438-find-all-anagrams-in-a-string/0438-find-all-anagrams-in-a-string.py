class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        seen = collections.defaultdict(int)
        for i in p:
            seen[i] += 1
        ans = []
        sub = collections.defaultdict(int)
        n = len(p)
        l = 0

        for i,val in enumerate(s):
            sub[val] += 1
            if sub == seen:
                ans.append(l)

            if (i - l + 1) >= n: 
                sub[s[l]] -= 1
                if sub[s[l]] == 0: del sub[s[l]]
                l += 1
            
        return ans
        

