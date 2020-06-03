# Q: There are 2N people a company is planning to interview. The cost of flying the i-th person to city A
#    is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].
# INPUT:  [[10,20],[30,200],[400,50],[30,20]] -
# OUTPUT: Minimum cost to fly every person to a city such that exactly N people arrive in each city.
# IDEA:   1. Put all of them to city A and calculate cost
#         2. Find the difference- i[1]-i[0], to find the cost required to move from city A to city B
#         3. Sort values in Step 2 and choose n//2 values
#         4. Find final sum: sum in step 1 + sum in step 3

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        s = 0
        a = []
        db = []
        for i in costs:
            a.append(i[0])
        for i in costs:
            db.append(i[1]-i[0])
        db.sort()
        s = sum(a)+sum(db[0:(len(costs)//2)])
        return s