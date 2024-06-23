class CircleQueue:
  def __init__(self,max_size):
    self.queue=[None]*max_size
    self.max_size=max_size
    self.rare=-1
    self.m_front=-1

  def isEmpty(self):
    return self.m_front==-1

  def isFull(self):
    if(self.rare+1)%self.max_size==self.m_front:
      return True
    return False

  def Enqueue(self, item):
    if self.isFull():
      return 
    if self.isEmpty():
      self.m_front=0
    self.rare=(self.rare+1)%self.max_size
    self.queue[self.rare]=item

  def Dequeue(self):
    if self.isEmpty():
      return
    self.queue[self.m_front]=None
    if self.rare==self.m_front:
      self.rare=self.m_front=-1
    else:
      self.m_front=(self.m_front+1)%self.max_size
    

  def front(self):
    if self.isEmpty():
      return
    return self.queue[self.m_front]


Q=CircleQueue(10)
for i in range(10):
  Q.Enqueue(i)
print(Q.queue)
Q.Dequeue()
print(Q.queue)
Q.Dequeue()
print(Q.queue)
Q.Enqueue(0)
print(Q.queue)
Q.Enqueue(0)
print(Q.queue)
Q.Enqueue(0)
print(Q.queue)
