class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for i in range(m-1):
            new = [1] * n

            for j in range(n-2, -1,-1):
                new[j] = new[j+1] + row[j]

            row = new

        return row[0]