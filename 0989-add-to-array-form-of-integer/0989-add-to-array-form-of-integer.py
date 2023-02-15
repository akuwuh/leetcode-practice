class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:  
        return [int(i) for i in str(int(''.join(map(str,num))) + k)]