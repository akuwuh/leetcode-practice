class Solution:
    def isHappy(self, n: int) -> bool:
         visit = set()

         while n not in visit:
             visit.add(n)
             n = self.sumofSquares(n)

             if n == 1:
                 return True
        
         return False
    
    def sumofSquares(self, n: int) -> int:
        out = 0

        while n: 
            dig = (n%10)
            dig = dig ** 2

            out += dig

            n = n // 10
        
        return out