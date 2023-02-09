class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        ans = 0
        groups2 = dict()
        keys = []
        for i in ideas:
            if i[0] in groups2:
                groups2[i[0]].add(i[1:])
            else:
                groups2[i[0]] = {i[1:]}
                keys.append(i[0])

        for ind,i in enumerate(keys):
            new = keys[ind+1:]
            for j in new:
                mut = len(groups2[i].intersection(groups2[j]))
                ans += (2 * (len(groups2[i]) - mut) * (len(groups2[j]) - mut))

        return ans