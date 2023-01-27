class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        sol = [[]]
        
        for i in nums:
            new = [x + [i] for x in sol] #makes new list of combinations w current i then add to sol
            sol += new
        return sol
        
        
        
'''
    First attempt
    
        sol = [[]]

            for i,val in enumerate(nums): #for every new number in the list, val is value of number and i is index and enumerate is the function taht allows us to keep track of both
                if i == 0: #if first element
                    sol.append([val]) #just append the values in list form
                    continue #if len of nums == 1, then break out of loop and return

                # for len(nums) > 1
                length = len(sol)
                sol.append([val]) #first append the next number

                x = 1
                while x < length:  #append every previous thing in sol list, using fixed variable length since len(sol) is dynamic as we keep appending. 
                                   #x is counter to keep track of prev elements and starts at 1 since we don't want to include [] being the first element
                    sol.append(sol[x] + [val]) #append current element (in list form) with currrent new number (also in list form) to the solution
                    x+=1 #increase counter 

            return sol
'''

    #Example Test Case:
    #[1,2,3,4,5]

    #[] -> [[]]

    #[1] -> [[],[1]]

    #---! Starts here !---

    #2
    #Current len(sol) = 2
    #[2] -> [[],[1],[2]] 
    #[1,2] -> [[],[1],[2],[1,2]]

    #3
    #Current len(sol) = 4
    #[3] -> [[],[1],[2],[1,2],[3]]
    #[1,3],[2,3] -> [[],[1],[2],[1,2],[3],[1,3],[2,3]]
    #[1,2,3] -> [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

    #[4] -> [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3],[4]]
    #[1,4],[2,4],[1,2,4] -> [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3],[4],[1,4],[2,4],[1,2,4]]
    #[3,4],[1,3,4],[2,3,4] -> [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3],[4],[1,4],[2,4],[1,2,4],[3,4],[1,3,4],[2,3,4]]
    #[1,2,3,4] -> [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3],[4],[1,4],[2,4],[1,2,4],[3,4],[1,3,4],[2,3,4],[1,2,3,4]]


    #[5]
    #[1,5],[2,5],[1,2,5] -> [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3],[4],[1,4],[2,4],[1,2,4],[3,4],[1,3,4],[2,3,4],[1,2,3,4],[1,5],[2,5],[1,2,5]]
    #[3,5],[1,3,5],[2,3,5],[1,2,3,5] -> [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3],[4],[1,4],[2,4],[1,2,4],[3,4],[1,3,4],[2,3,4],[1,2,3,4],[1,5],[2,5],[1,2,5],[3,5],[1,3,5],[2,3,5],[1,2,3,5]]
    #[4,5],[1,4,5],[2,4,5],[1,2,4,5],[3,4,5],[1,3,4,5],[2,3,4,5] -> ...
    #[1,2,3,4,5]