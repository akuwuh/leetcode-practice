class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        stack1 = []
        stack2 = []

        for i in range(max(len(s), len(t))):

            if i <len(s) and len(s) !=0: #
                if s[i] == '#':
                    if stack1: stack1.pop()
                else:
                    stack1.append(s[i])

            if i < len(t) and len(t) != 0:
                if t[i] == '#':
                    if stack2: stack2.pop()
                else:
                    stack2.append(t[i])
        
        return stack1 == stack2
            
            
