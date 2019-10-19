class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    # if None in self.storage:
    #   for index, char in enumerate(self.storage):
    #     if char == None:
    #       self.storage[index] = item
    #       break
    # else: 
    #   if self.current == 0:
    #     self.storage[0] = item
    #     self.current = item
    #   else:
    #     if self.storage.index(self.current) == self.capacity:
    #       self.storage[0] = item
    #       self.current = item
    #     else:
    #       self.storage[self.storage.index(self.current) + 1] = item
    #       self.current = item
    self.storage[self.current] = item
    
    self.current = 0 if self.current + 1 == self.capacity else self.current + 1
    
  def get(self):
    return [item for item in self.storage if item != None]