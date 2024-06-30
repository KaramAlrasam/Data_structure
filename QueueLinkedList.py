class Node:
  def __init__(self, data):
    self.data=data
    self.next=None

class QueueLinkedList:
  def __init__(self):
    self.head=None
    self.tail=None

  def Enqueue(self, data):
    new_node=Node(data)
    if self.isEmpty():
      self.head=self.tail=new_node
      return
    
    self.tail.next=new_node
    self.tail=new_node

  def Dequeue(self):
    if self.isEmpty():
      return
    if self.head.data==self.tail.data:
      self.head=self.tail=None
      return
    self.head=self.head.next

  def isEmpty(self):
    if self.head==None and self.tail==None:
      return True
    return False

  def frontValue(self):
    if self.isEmpty():
      return
    return self.head.data

QLL=QueueLinkedList()
for i in range(7):
  QLL.Enqueue(i)

while not QLL.isEmpty():
  print(QLL.frontValue())
  QLL.Dequeue()