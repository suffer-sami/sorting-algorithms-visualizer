from enum import Enum

class State(Enum):
    UNSORTED = 1
    BEING_SORTED = 2
    SORTED = 3

class Bar:
    def __init__(self, val):
        self.val = val 
        self.state = State.UNSORTED

    def __gt__(self, other):
        return self.val > other.val
    
    def __lt__(self, other):
        return self.val < other.val
    
    def __eq__(self, other):
        return self.val == other.val