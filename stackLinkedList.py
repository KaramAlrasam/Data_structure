class Node:
  def __init__(self, data):
    self.data=data
    self.next=None

class stackLinkedList:
  def __init__(self):
    self.top=None

  def push(self, data):
    new_node=Node(data)
    if self.isEmpty():
      new_node.next=self.top
      self.top=new_node
      new_node.next=None
      return
    new_node.next=self.top
    self.top=new_node

  def pop(self):
    if self.isEmpty():
      return
    self.top=self.top.next

  def topValue(self):
    if self.isEmpty():
      raise Exception ("There are no items")
    return self.top.data

  def isEmpty(self)->bool:
    if self.top==None:
      return True
    return False
SLL=stackLinkedList()

for i in range(7):
  SLL.push(i)

while not SLL.isEmpty():
  print(SLL.topValue())
  SLL.pop()