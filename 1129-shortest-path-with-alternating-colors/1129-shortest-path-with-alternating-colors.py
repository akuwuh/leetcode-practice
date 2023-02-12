class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        radj, badj = defaultdict(list), defaultdict(list) #adjacency lists

        for a,b in redEdges: #for each node a -> b
            radj[a] += [b]
        for a,b in blueEdges: #for each node a -> b
            badj[a] += [b]

        r_seen,b_seen = {0}, {0}
        q = deque([[0,0,-1]]) # 0 = r, 1 = b
        ans = [-1]*n
        ans[0] = 0

        while q:
            node, dist, colour = q.popleft()
            if colour <= 0: # red
                for i in badj[node]: #search through list of possible next nodes has to be in blue since started in red
                    if i not in b_seen: #next node valid to search
                        ans[i] = min(dist + 1, ans[i]) if ans[i] != -1 else dist + 1
                        q.append([i,dist + 1,1]) #add to search queue
                        b_seen.add(i)
            if colour == 1 or colour == -1: #blue
                for i in radj[node]: #search through list of possible next nodes has to be in blue since started in red
                    if i not in r_seen: #next node valid to search
                        ans[i] = min(dist + 1, ans[i]) if ans[i] != -1 else dist + 1
                        q.append([i,dist + 1,0]) #add to search queue
                        r_seen.add(i)
        
        return ans





        
