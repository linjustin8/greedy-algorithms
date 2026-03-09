# greedy.py
from collections import deque

class Greedy:
    def __init__(self, k: int, requests: list):
        self.capacity = k
        self.sequence = requests
        
    
    def fifo(self) -> int:  # slide 39
        cache = deque()
        misses = 0
        
        
        pass
    
    def lru(self) -> int: # slide 39
        pass
    
    def optff(self) -> int: # slide 40
        pass