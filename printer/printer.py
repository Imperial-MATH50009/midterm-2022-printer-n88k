"""Implement the printer."""
from collections import deque


class Document:
    def __init__(self, strings=()):
        self.queue=deque(strings)
    
    def append(self,string):
        self.queue.append()

