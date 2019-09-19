import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Queue:
  def __init__(self):
    # Why is our DLL a good choice to store our elements?
    self.storage = DoublyLinkedList()

  def enqueue(self, item):
    self.storage.add_to_tail(item)

  def dequeue(self):
      return self.storage.remove_from_head()
  
  def len(self):
    return self.storage.length


q = Queue()
print(q.enqueue(3))
print(q.storage)
print(q.dequeue())