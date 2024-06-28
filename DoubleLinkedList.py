class Node:
  def __init__(self, data):
    self.data=data
    self.prev=None
    self.next=None

class DoubleLinkedList:
  def __init__(self):
    self.head=None

  def append(self, data):
    new_node=Node(data)
    if not self.head:
      self.head=new_node
      return
    lasted_node=self.head
    while lasted_node.next:
      lasted_node=lasted_node.next
    new_node.prev=lasted_node
    lasted_node.next=new_node

  def display(self):
    curr=self.head
    while curr:
      print(curr.data,end=" -> ")
      curr=curr.next
    print(None)

  def insert(self, data, pos):
    new_node=Node(data)
    if self.head==None:
      self.append(data)
      return
    if pos==0:
      new_node.next=self.head
      self.head.prev=new_node
      self.head=new_node
      return
    lasted_node=self.head
    for _ in range(pos):
      if lasted_node.next==None:
        break
      lasted_node=lasted_node.next
    if lasted_node.next==None:
      self.append(data)
      return
    new_node.prev=lasted_node
    lasted_node.prev.next=new_node
    new_node.next=lasted_node
    lasted_node.prev=new_node
      
  def remove(self, data):
    curr=self.head
    while curr:
      if curr.data==data:
        if curr.prev:
          curr.prev.next=curr.next
        if curr.next:
          curr.next.prev=curr.prev
        if curr==self.head:
          self.head=self.head.next
          self.head.prev=None
      curr=curr.next

  def reverse_display(self):
    curr=self.head
    while curr.next:
      curr=curr.next
    while curr:
      print(curr.data, end=" <- ")
      curr=curr.prev
    print()

  def remove2(self,pos):
    if not self.head:
      return
    if pos==0:
      self.head=self.head.next
      self.head.prev=None
      return
    lasted_node=self.head
    for _ in range(pos):
      if lasted_node.next ==None:
        break
      lasted_node=lasted_node.next
    if lasted_node.next:
      lasted_node.prev.next=lasted_node.next
      lasted_node.next.prev=lasted_node.prev
      return
    lasted_node.prev.next=None
    
    
        
    
      


DLL=DoubleLinkedList()
for i in range(6):
  DLL.append(i)

DLL.display()
DLL.insert(10,6)
DLL.display()
DLL.remove(3)
DLL.display()
DLL.reverse_display()


DLL.remove2(1000)
DLL.display()
DLL.append(10)
DLL.append(11)
DLL.append(12)
DLL.append(13)
DLL.display()
DLL.insert(3,3)
DLL.display()
DLL.insert(6,6)
DLL.insert(7,7)
DLL.insert(8,8)
DLL.insert(9,9)
DLL.display()
DLL.remove(0)
DLL.display()
