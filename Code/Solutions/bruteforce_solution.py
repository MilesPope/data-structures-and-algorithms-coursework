from model import ProblemInstance, Event
from pathlib import Path
import itertools


def bruteforce(problem):
    list = problem.events
    num = problem.event_count


    max_enjoy = -1
    max_enjoy_subset = ()
    # print("Calculating solution from every possible combination.....")
    for i in range(num+1):
        for subset in itertools.combinations(list, i): # Calculates every possible combination of every length in the loop
            mon_sum = 0
            enjoy = 0
            for event in subset: # Sums events cost and enjoyment in the subset
                mon_sum += event.cost
                enjoy += event.e_value
            if enjoy > max_enjoy and mon_sum <= problem.cost_constraint: # checks for if it is currently the most optimal event subset
                max_enjoy = enjoy
                max_enjoy_subset = subset
                
    return max_enjoy_subset   
            
        
