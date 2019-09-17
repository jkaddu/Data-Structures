import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Queue:
  def __init__(self):
    self.size = 0
    # Why is our DLL a good choice to store our elements?
    self.storage = []

  def enqueue(self, item):
    self.storage.append(item)
  
  def dequeue(self):
    if len(self.storage):
      return self.storage.pop(0)

  def len(self):
    return len(self.storage)


q = Queue()
print(q.enqueue(3))
print(q.storage)
print(q.dequeue())