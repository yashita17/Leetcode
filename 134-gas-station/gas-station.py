class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        start = 0
        curr_pet = 0
        prev_pet = 0
        for i in range(len(gas)):
            curr_pet += gas[i] - cost[i]
            if curr_pet < 0:
                start = i+1
                prev_pet += curr_pet
                curr_pet = 0
        if curr_pet + prev_pet >= 0:
            return start 
        else:
            return -1
        