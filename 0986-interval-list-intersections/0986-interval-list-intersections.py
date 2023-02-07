class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        i = 0
        j = 0 
        ans = []

        while i < len(firstList) and j < len(secondList):
            
            if(max(firstList[i][0], secondList[j][0]) <=  min(firstList[i][1], secondList[j][1])):
                ans.append([max(firstList[i][0], secondList[j][0]), min(firstList[i][1], secondList[j][1])])

        
            if firstList[i][1] < secondList[j][1]:
                i+=1
            
            else:

                j+=1
        
        return ans
            

        #[[0,2],[5,10],[13,23],[24,25]]

        #[[1,5],[8,12],[15,24],[25,26]]