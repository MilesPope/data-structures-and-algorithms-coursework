from model import ProblemInstance, Event
from pathlib import Path
from Solutions.bruteforce_solution import bruteforce
from Solutions.dynamic_solution import dynamic_event_planner
from time import perf_counter

THIS_DIR = Path(__file__).resolve().parent.parent # Get to dir containing src and sample_inputs
found_file = False
while not found_file:
    INPUT_FILE = input("Specify input file to use: \n")
    try:
        problem = ProblemInstance.from_file(rf'{THIS_DIR}/Input_Files/{INPUT_FILE}')
        found_file = True
    except:
        print("File not found, ensure it is in /Input_Files/ and has .txt file extention")

print("========================================")
print("GROUP 8 - EVENT PLANNER - RESULTS")
print("========================================")

print(f"Input File: {INPUT_FILE}")

print(f"Available Time: {problem.time_constraint}")
print(f"Available Budget: £{problem.cost_constraint}")
print(f"\n--- BRUTE FORCE ALGORITHM --- ")

tic = perf_counter()
events = bruteforce(problem)
toc = perf_counter()
duration = toc - tic
print(f"Selected Activities")

total_enjoyment = 0
total_time = 0
total_cost = 0

for event in events:
    print(f"\t- {event.name} ({event.duration} hours, £{event.cost}, enjoyment {event.e_value})")
    total_enjoyment += event.e_value
    total_time += event.duration
    total_cost += event.cost
    
print (f"Total Enjoyment: {total_enjoyment}")
print (f"Total Time Used: {total_time} hours")
print (f"Total Cost: £{total_cost}")
print (f"Execution time: {duration:0.9f}")

### Dynamic Approach ###
print("\n--- DYNAMIC PROGRAMMING ALGORITHM ---")
# Get the solution
tic = perf_counter()
max_e_value, chosen_events = dynamic_event_planner(problem)
toc = perf_counter()
duration = toc - tic

total_time, total_cost = 0, 0

print("Chosen activities:")

for event in chosen_events:
    print("\t- " + event.to_str())
    total_cost += event.cost
    total_time += event.duration

print (f"Total Enjoyment: {max_e_value}")
print (f"Total Time Used: {total_time} hours")
print (f"Total Cost: £{total_cost}")
print (f"Execution time: {duration:0.9f}")