import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
  def __init__(self):
    self.size = 0
    # Why is our DLL a good choice to store our elements?
    self.storage = DoublyLinkedList()

  def push(self, item):
    self.storage.add_to_head(item)
  
  def pop(self):
    if self.size > 0:
      self.size -= 1
      return self.storage.remove_from_head()

  def len(self):
    return self.storage.__len__()
