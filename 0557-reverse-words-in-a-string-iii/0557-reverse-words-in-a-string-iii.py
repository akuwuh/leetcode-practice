class Solution:
    def reverseWords(self, s: str) -> str:
        x = s.split(' ')
        new = ""
        for i in x:
            new += i[::-1] + " "
                
        return new[:-1]