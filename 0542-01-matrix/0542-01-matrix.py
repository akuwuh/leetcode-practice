class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = deque()
        visited = set()
        dir = [[0,1], [1,0], [0,-1], [-1,0]]

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    q.append((i,j)) # append to deque if is equal to 0
                    visited.add((i,j))

        while q:
            i,j = q.popleft()

            for x in dir:
                newi,newj = i + x[0], j + x[1]

                if (newi >= 0 and newi < len(mat)) and (newj >=0 and newj < len(mat[0]) and (newi,newj) not in visited):
                    mat[newi][newj] = mat[i][j] + 1
                    q.append((newi,newj))
                    visited.add((newi,newj))
        return mat









        
        