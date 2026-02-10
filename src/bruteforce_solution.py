from model import ProblemInstance, Event
import itertools

message = " Group 8 Bruteforce Solution "
print(message.center(100, '#'))


print("Loading from file.....", end='') # Loads file
problem = ProblemInstance.from_file(r'input_small.txt')
print(' success')

list = problem.events
num = problem.event_count


combinations = []
max_enjoy = -1
max_enjoy_subset = []
print("Calculating solution from every possible combination.....", end='')
for i in range(num+1):
    for subset in itertools.combinations(list, i):
        mon_sum = 0
        enjoy = 0
        for event in subset:
            mon_sum += event.cost
            enjoy += event.e_value
        if enjoy > max_enjoy and mon_sum <= problem.cost_constraint:
            max_enjoy = enjoy
            max_enjoy_subset = subset
            
print(" success")     
            
        

message = " Optimal Solution: "
print(message.center(100, '#'))

count = 1
for event in max_enjoy_subset:
    print(f"Event {count}: Name: {event.name}, Cost: {event.cost}, Enjoyment: {event.e_value}")
    count += 1

