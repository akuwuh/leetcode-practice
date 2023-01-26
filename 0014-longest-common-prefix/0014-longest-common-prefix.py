class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        for i in zip(*strs):
            if len(set(i)) == 1:
                ans = ans + i[0]
            else:
                return ans
        return ans


        