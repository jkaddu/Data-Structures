import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Queue:
  def __init__(self):
    self.size = 0
    # Why is our DLL a good choice to store our elements?
    self.storage = DoublyLinkedList()

  def enqueue(self, item):
    self.storage.add_to_tail(item)
    self.size += 1

  def dequeue(self):
    if self.size > 0:
      self.size -= 1
      return self.storage.remove_from_head()
    else:
      return None

  def len(self):
    return self.size


q = Queue()
print(q.enqueue(3))
print(q.storage)
print(q.dequeue())