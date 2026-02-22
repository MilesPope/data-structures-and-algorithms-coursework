from model import ProblemInstance, Event
from pathlib import Path
from solutions.bruteforce_solution import bruteforce
from solutions.dynamic_solution import dynamic_event_planner
import itertools
INPUT_FILE = 'input_small.txt'
THIS_DIR = Path(__file__).resolve().parent
print("========================================")
print("GROUP 8 - EVENT PLANNER - RESULTS")
print("========================================")

print(f"Input File: {INPUT_FILE}")

problem = ProblemInstance.from_file(rf'{THIS_DIR}\{INPUT_FILE}')

print(f"Available Time: {problem.time_constraint}")
print(f"Available Budget: £{problem.cost_constraint}")
print(f"\n--- BRUTE FORCE ALGORITHM --- ")

events = bruteforce(problem)
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
