"""Implement the printer."""
from collections import deque


class Document:
    def __init__(self, strings=[]):
        self.queue = deque(strings)

    def append(self, string):
        self.queue.append(string)

    def print(self):
        return self.queue.popleft()

    def __len__(self):
        return len(self.queue)


class Printer:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, doc):
        self.queue.append(doc)

    def cancel(self):
        self.queue.popleft()

    def __len__(self):
        return len(self.queue)

    def pages(self):
        return sum([len(doc) for doc in self.queue])

    def print(self):
        first_doc = self.queue[0]
        page = first_doc.print()
        if not first_doc:
            self.queue.popleft()
        return page
