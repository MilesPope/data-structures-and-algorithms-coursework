import unittest
from model import Event, ProblemInstance
from Solutions.bruteforce_solution import bruteforce
from Solutions.dynamic_solution import dynamic_event_planner
from pathlib import Path

THIS_DIR = Path(__file__).resolve().parent.parent # Get to dir containing src and sample_inputs
INPUT_FILE = 'input_small.txt'
problem = ProblemInstance.from_file(rf'{THIS_DIR}/Input_Files/{INPUT_FILE}')
found_file = True


class TestEventClass(unittest.TestCase):
    """
    Unit tests for the event class. Example inputs:
    Welcome-Dinner 2 40 75
    Quiz-Night 2 30 60
    Movie-Night 3 35 80
    Sports-Day 4 50 100
    Art-Class 2 60 90
    Karaoke 2 45 85
    Bowling 3 70 105
    Cooking-Workshop 3 80 120
    Beach-Outing 5 90 140
    Concert-Trip 4 110 160
    """
    def test_init(self):
        """
        Test the initialisation of the class
        """
        new_event = Event("Welcome-Dinner", 2, 40, 75)
        self.assertIsNotNone(new_event)
        self.assertIsInstance(new_event, Event)

    def test_getters(self):
        """
        Test the getter methods for the function
        """
        new_event = Event("Welcome-Dinner", 2, 40, 75)
        self.assertEqual(new_event.name, "Welcome-Dinner")
        self.assertEqual(new_event.duration, 2)
        self.assertEqual(new_event.cost, 40)
        self.assertEqual(new_event.e_value, 75)

    def test_from_str(self):
        """
        Test that an event instance can be instantiated from a valid string
        """
        test_string = "Welcome-Dinner 2 40 75"
        new_event = Event.from_str(test_string)
        self.assertEqual(new_event.name, "Welcome-Dinner")
        self.assertEqual(new_event.duration, 2)
        self.assertEqual(new_event.cost, 40)
        self.assertEqual(new_event.e_value, 75)

class TestProblemInstance(unittest.TestCase):
    """
    Unit tests for the ProblemInstance class.
    """
    def setUp(self):
        THIS_DIR = Path(__file__).resolve().parent.parent # Get to dir containing src and sample_inputs
        self.problem = ProblemInstance.from_file(rf'{THIS_DIR}/Input_Files/input_10.txt')
        return super().setUp()
    def test_from_file(self):
        """
        Test that a ProblemInstance can be created from a file with relevant information
        """
        self.assertIsNotNone(self.problem)
    
    def test_initialisation(self):
        """
        Test that no information is destroyed and is parsed correctly 
        """
        self.assertEqual(self.problem.event_count, 10)
        new_event = Event("Welcome-Dinner", 2, 40, 75)
        self.assertEqual(new_event, self.problem.events[0])
    
    def test_single_event_over_budget(self):
        '''
        Test that for a single event over budget, an empty list is returned
        '''
        e1 = Event('A', 1, cost=100, e_value=10)
        problem = ProblemInstance(events=[e1], event_count=1, cost_constraint=20, time_constraint=0)
        result = bruteforce(problem)
        self.assertEqual(result, ())
    
    def test_single_event_under_budget(self):
        '''
        Test that for a single event under budget, the event itself is returned
        '''
        e1 = Event('A', 1, cost=10, e_value=10)
        problem = ProblemInstance(events=[e1], event_count=1, cost_constraint=20, time_constraint=0)
        result = bruteforce(problem)
        self.assertEqual(result, (e1,))
    
    def test_best_combination(self):
        '''
        Test that for multiple events it chooses the best events
        '''
        e1 = Event('A', 1, cost=10, e_value=10)
        e2 = Event('B', 1, cost=5, e_value=10)
        e3 = Event('C', 1, cost=5, e_value=10)
        e4 = Event('D', 1, cost=10, e_value=10)
        problem = ProblemInstance(events=[e1, e2, e3, e4], event_count=4, cost_constraint=20, time_constraint=0)
        result = bruteforce(problem)
        self.assertEqual(result, (e1, e2, e3))
        
class TestDynamicApproach(unittest.TestCase):
    """
    Unittest for dyanamic solution
    """
    def test_single_event_over_budget_dp(self):
        '''
        Test that for a single event over budget, an empty list is returned
        '''
        e1 = Event('A', 1, cost=100, e_value=10)
        problem = ProblemInstance(events=[e1], event_count=1, cost_constraint=20, time_constraint=0)
        result = dynamic_event_planner(problem)[1]
        self.assertEqual(result, [])
    
    def test_single_event_under_budget_dp(self):
        '''
        Test that for a single event under budget, the event itself is returned
        '''
        e1 = Event('A', 1, cost=10, e_value=10)
        problem = ProblemInstance(events=[e1], event_count=1, cost_constraint=20, time_constraint=0)
        result = dynamic_event_planner(problem)[1]
        self.assertEqual(result, [e1,])
    
    def test_best_combination_dp(self):
        '''
        Test that for multiple events it chooses the best events
        '''
        e1 = Event('A', 1, cost=10, e_value=10)
        e2 = Event('B', 1, cost=5, e_value=10)
        e3 = Event('C', 1, cost=5, e_value=10)
        e4 = Event('D', 1, cost=10, e_value=5)
        problem = ProblemInstance(events=[e1, e2, e3, e4], event_count=4, cost_constraint=20, time_constraint=0)
        result = dynamic_event_planner(problem)[1]
        self.assertCountEqual(result, [e1, e2, e3])
        