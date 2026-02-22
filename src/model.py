"""
File containing classes to be used in the event planner solution including:
- Event
- Problem Instance
"""
class Event:
    """
    Event class:
    Attribues:
    - duration: time in hours the event takes. Not called time to avoid conflicts with time module
    - cost: cost to attend the event in pounds
    - e_value: entertainment value of the activity
    Methods: 
    - Getters for each field
    - from_str: create an instance of the event from a relevant string
    """
    def __init__(self, name:str, duration: int, cost: int, e_value: int):
        self._name = name
        self._duration = duration
        self._cost = cost
        self._e_value = e_value

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Event):
            # Don't attempt to compare against unrelated types
            return NotImplemented
        
        return (self.name == other.name 
                and self.duration == other.duration
                and self.cost == other.cost
                and self.e_value == other.e_value
                )


    # Getters. Setters unrequired - fields are final
    @property
    def name(self):
        return self._name
    @property
    def duration(self):
        return self._duration
    @property
    def cost(self):
        return self._cost
    @property
    def e_value(self):
        return self._e_value


    @classmethod
    def from_str(cls, string: str) -> "Event": # type: ignore
        """
        Create an instance of the event class from a string containing relevant information
        
        :param string: A string in format '{name} {duration} {cost} {e_value}'
        :type string: str
        :return: loaded instance of the event
        :rtype: Event
        """
        try:
            tokens = string.split(" ")
            return cls(tokens[0], int(tokens[1]), int(tokens[2]), int(tokens[3]))
        except TypeError:
            print("Missing a parameter")

    def to_str(self) -> str:
        """
        Convert instance information into a string with the following format:
         Name (duration hours, £cost, enjoyment e_value)
        i.e.:
            Game-Night (3 hours, £80, enjoyment 120)
        """
        return f"{self.name} ({self.duration} hours, ${self.cost}, enjoyment {self.e_value})"

class ProblemInstance:
    """
    An instance of the problem which contains data relevant 
    to the events available and constraints to the day.
    Attributes:
    - time_contraint: the available time in the problem instance
    - cost_contraint: the available cost in the problem instance
    - events: the available events in the problem instance
    - event_count
    Methods:
    - Getters
    - from_file: create a problem instance from a relevant file
    """
    def __init__(self, time_constraint: int, cost_constraint: int, events: list, event_count: int) -> None:
        self._time_constraint = time_constraint
        self._cost_constraint = cost_constraint
        self._events = events
        self._event_count = event_count

    # Getters. Setters unrequired - fields are final
    @property
    def time_constraint(self):
        return self._time_constraint
    @property
    def cost_constraint(self):
        return self._cost_constraint
    @property
    def events(self):
        return self._events
    @property
    def event_count(self):
        return self._event_count
        
    @classmethod
    def from_file(cls, file_name: str) -> "ProblemInstance":
        """
        Create an instance of the ProblemInstance class from a file containing relevant information
        • Line 1: A single integer n, the number of activities available.
        • Line 2: Two integers separated by a space: T (maximum available time in 
        hours) and B (maximum budget in pounds). You may choose to enforce only 
        one of these constraints in your core implementation, but both values should 
        be present in the input file for completeness. When dealing with one 
        constraint, simply ignore the other value. This helps us having to deal with just 
        one format for the input file.
        • Lines 3 to (n+2): Each line describes one activity, in the following format: 
            o Activity Name (a single word or a hyphen-separated phrase with no 
            spaces, e.g., Board-Games or Museum-Trip)
            o Time Required (a positive integer, in hours)
            o Cost (a positive integer, in pounds)
            o Enjoyment Value (a positive integer)
        
        :param file_name: Name of the .txt file containing relevant information. We assume the file is in the same directory
        :type file_name: str
        :return: loaded instance of the class
        :rtype: ProblemInstance
        """
        with open(file_name, 'r') as file:
            events = []
            for line_number, line in enumerate(file):
                # Event count is on line 1
                if line_number == 0:
                    event_count = int(line.strip())
                # Constraints are on line 2 in format '{Time} {Budget}'
                elif line_number == 1:
                    constraints = line.strip().split() # [{Time}, {Budget}]
                    time_constraint = int(constraints[0])
                    cost_constraint = int(constraints[1])
                # Other lines are events
                else:
                    events.append(Event.from_str(line.strip()))
            
            return ProblemInstance(time_constraint, cost_constraint, events, event_count) # type: ignore
