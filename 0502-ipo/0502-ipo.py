import heapq as hq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        #notes: 
        # k distinct projects at most
        # given:
            # profits array where profits[i] denotes pure profits for ith project
            # capital array where capital[i] denotes amount of capital needed to start the ith project
            # start with w capital, capital increases when project completes (profits[i] + w)

        
        # goal: 
            # pick from at most k projects to get most profits
        
        # approach brainstorm:

        # starting with w capital, we must choose k options from profits/capitals to maximize w
        # questions to ask:
        # which projects can i buy with my current capital
        # which one will give the most profits from what I can afford at the moment?

        # rinse and repeat until k is up

        # now we need to consider:
         
        # current capital -> what can i buy (can be capital requirements) -> which has the most profits?
        # so how do i store capital requirement and profits such that they are easily searchable for the current given capital?

        # also if current capital is not enough to reach next capital requirement, then will have to keep searching within current capital requirement

        # so as we progress in capital gains, there will be new possibilities available. each iteration of k will introduce more possibilities for profits, whether greater or larger

        # maybe we can use the idea of prefix to keep track of be possible option for each new possibility that opens up?

        # so how do we determine the next best outcome?
        # # of possible outcomes only increases if our capital gain meets the next available capital requirement
        # then that means we take the outcome of all previous ones and the new ones to determine the best outcome from that 

        # maybe w/ each iteration, update outcomes? w/ profits?

        # maybe if new capital requirement encountered, append the list of profits available for that outcome and every new one in between. then from there we can pick and choose the max one

        # what about if new capital requirement not encountered?
        # then next possible outcome will just be the next max within the list of current outcomes

        # if we choose an outcome to be added to our capital, then we must pop it. capital will always increase.

        # so the general process (hoping that it doesn't TLE):

        # starting w/ w capital
        # we will make a dictionary that stores the capital requirement as a key and all of the profits of it
        # we will also make a list of sorted capital requirement to keep track of the current one that we are on with respect to capital gains. we can also increment without missing any in between elements
        # we will also create a priority queue to append the newly added profits possibility with respect to its capital requirement the heap will go through O(nlogn) to add new elements
        # iterate k times (anount of time we increase capital)
        # each iteration we:
        # compare capital if new capital gain can be achieved then:
            # iterate through the dictionary to append new elements to heap in O(nlogn) where n is the amount of new potential profits
        # if not then just pop next best profits
        # pop off top of priority queue getting max profits for best possible outcome in the current moment (heap will organize)
        # add to capital 

        #time complexity analysis:
        # k is the amount of cap req to append
        # append + heapify = O(k) * O(logn) = O(klogn) * creating a new heap everytime
        
        # pop + append each element = O(logn) + O(nlogn) where n is thenumber of elements

        # then most optimal storing process is:
        # have list of element, append more if needed
        # heapify
        # when pop you pop from the heap but the original list stays, we just keep track of the index to be popped off
        # can use set hashing for that.
        # alright lets start implementing

        p = 0 # pointer for the keys (curr cap)
        cap = defaultdict(list)

        for i,val in enumerate(capital):
            cap[val].append(profits[i])

        keys = sorted(set(capital))

        prof = [] # profit array to keep track of all profits
        for i in range(min(k,len(capital))):
            while p < len(keys) and keys[p] <= w and keys[p] in cap:
                for i in cap[keys[p]]:
                    heapq.heappush(prof, -i)
                cap.pop(keys[p])
                p+=1

            if not prof:
                return w

            add = -heapq.heappop(prof) # adds prof to the top 
            w+= add
        return w
        



















         



