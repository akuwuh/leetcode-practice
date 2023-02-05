class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        ans = []
        
        vowels = {
            'a': 0,
            'e': 0,
            'o': 0,
            'i': 0,
            'u': 0,
        }
        
        pref = [0]
        
        for i in range(len(words)): #iterate through queries
            add = 0
            if words[i][0] in vowels and words[i][-1] in vowels:
                add = 1

            
            pref.append(pref[i] + add)
                        
        print(pref)
        
        for i in queries:
            l = i[0]
            r = i[1]

            ans.append(pref[r+1] - pref[l])
            
        return ans