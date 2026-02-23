import unittest
from model import Event, ProblemInstance
from Solutions.bruteforce_solution import bruteforce


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
    def test_from_file(self):
        """
        Test that a ProblemInstance can be created from a file with relevant information
        """
        new_problem_instance = ProblemInstance.from_file("../sample_inputs/input_10.txt")
        self.assertIsNotNone(new_problem_instance)
    
    def test_initialisation(self):
        """
        Test that no information is destroyed and is parsed correctly 
        """
        new_problem_instance = ProblemInstance.from_file("../sample_inputs/input_10.txt")
        self.assertEqual(new_problem_instance.event_count, 10)
        new_event = Event("Welcome-Dinner", 2, 40, 75)
        self.assertEqual(new_event, new_problem_instance.events[0])
class TestBruteForceSolution(unittest.TestCase):
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
        
        
        
        