"""
Top down approach to finding an optimal solution to a problem instance
"""
from model import ProblemInstance, Event
from pathlib import Path

def top_down_approach(budget, e_values, e_costs, e_names, e_durations, num_of_events, budget_memory):
    """
    The only parameters that change in the recusrive solution are the num_of_events and the budget. 
    Using a 2D array to store the maximum value we can get using items available.
    """
    # Base case:
    if num_of_events == 0 or budget == 0:
        return 0
    
    
    # Memo lookup - if we've already computed the subproblem we don't have to again
    if budget_memory[num_of_events][budget] != -1:
        # Return pre-calculated result
        return budget_memory[num_of_events][budget]
    
    # Initialise an empty variable to store the cost of chosen event
    chosen_event = 0

    # If event fits in budget
    if e_costs[num_of_events-1] <= budget:
        e_index = num_of_events - 1
        # Get the cost of the event
        cost = e_costs[e_index]
        # Make a recursive call with the updated sub-problem with the chosen event removed: "whats the maximum enjoyment using the first num_of_events excluding the taken" within the budget
        chosen_event = (
            e_values[e_index] + 
            top_down_approach(
                budget-cost, 
                e_values,
                e_costs,
                e_names,
                e_durations,
                num_of_events-1,
                budget_memory
            )
        )

    # If not, skip event, make a recursive call with the event removed
    not_chose = top_down_approach(budget, e_values, e_costs, e_names, e_durations, num_of_events - 1, budget_memory)

    # Place result into budget memory, choose the higher value
    budget_memory[num_of_events][budget] = max(chosen_event, not_chose)
    
    return budget_memory[num_of_events][budget]

def reconstruct_solution(budget, e_values, e_costs, e_names, e_durations, num_of_events, budget_memory):
    chosen_events = []

    while num_of_events > 0 and budget > 0:
        index = num_of_events - 1
        # Check states are computed
        if budget_memory[num_of_events][budget] == -1:
            top_down_approach(budget, e_values, e_costs, e_names, e_durations, num_of_events-1, budget_memory)

        current = budget_memory[num_of_events][budget]

        # If the current event fits:
        if e_costs[index] <= budget:
            remaining = budget - e_costs[index]

            if budget_memory[num_of_events - 1][remaining] == -1:
                # If we haven't computed this path, do so.
                budget_memory[num_of_events - 1][remaining] = top_down_approach(remaining, e_values, e_costs, e_names, e_durations, num_of_events-1, budget_memory)

            # Calculate the e_value if the event was taken
            taken_val = e_values[index] + budget_memory[num_of_events-1][remaining]
            # If equal to current it must have been taken
            if current == taken_val:
                chosen_events.append(
                    Event(
                        e_names[index], e_durations[index], e_costs[index], e_values[index]
                    )
                )
                budget -= e_costs[index]
                num_of_events -= 1
                continue
        # Event must have been skipped
        num_of_events -= 1

    return chosen_events

def dynamic_event_planner(problem_instance: ProblemInstance):
    # Initialise constraints and arrays from the problem instance
    budget = problem_instance.cost_constraint
    e_values = [event.e_value for event in problem_instance.events][::-1]
    e_costs  = [event.cost for event in problem_instance.events][::-1]
    e_names =  [event.name for event in problem_instance.events][::-1]
    e_durations = [event.duration for event in problem_instance.events][::-1]
    num_of_events = problem_instance.event_count
    # Table for results to be checked:
    budget_memory = [[-1] * (budget + 1) for _ in range(num_of_events + 1)]
    # Calculate the maximum entertainment value we can acheive in the solution space
    max_value = top_down_approach(budget, e_values, e_costs, e_names, e_durations, num_of_events, budget_memory)
    # Reconstruct the solution we got to get the events that we chose using the budget memory
    chosen = reconstruct_solution(budget, e_values, e_costs, e_names, e_durations, num_of_events, budget_memory)
    return max_value, chosen
