class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #[[1,3,5,7],[10,11,16,20],[23,30,34,60]]

        l,r = 0, len(matrix)*len(matrix[0]) -1
        c = len(matrix[0])

        while l <= r:
            m = (l + r)//2

            print("L = " + str(l))
            print("R = " + str(r))
            print("M = " + str(m))

            if matrix[m//c][m%c] == target:
                return True
            elif matrix[m//c][m%c] > target:
                r = m-1
            else:
                l = m+1

            print()


        return False