from enum import Enum

class State(Enum):
    UNSORTED = 1
    BEING_SORTED = 2
    SORTED = 3
    PIVOT = 4

class Bar:
    def __init__(self, val, state=State.UNSORTED):
        self.val = val 
        self.state = state

    def __gt__(self, other):
        return self.val > other.val
    
    def __lt__(self, other):
        return self.val < other.val
    
    def __eq__(self, other):
        return self.val == other.val
    
    def __ge__(self, other):
        return self.val >= other.val
    
    def __le__(self, other):
        return self.val <= other.val