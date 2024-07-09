class CQ:
  def __init__(self, max_size):
    self.queue=[None]*max_size
    self.max_size=max_size
    self.front=-1
    self.rare=-1

  def Enqueue(self, data):
    if self.isFull():
      return
    if self.isEmpty():
      self.front=0
    self.rare=(self.rare+1)%self.max_size
    self.queue[self.rare]=data

  def Dequeue(self):
    if self.isEmpty():
      return
    self.queue[self.front]=None
    if self.front==self.rare:
      self.front=self.rare=-1
      return
    self.front=(self.front+1)%self.max_size

  def displayFrontValue(self):
    if self.isEmpty():
      return
    return self.queue[self.front]

  def isFull(self):
    return (self.rare+1)%self.max_size==self.front

  def isEmpty(self):
    return self.front==-1

